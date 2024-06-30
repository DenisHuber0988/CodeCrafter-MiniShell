import os


class Handler:

    ERROR_MESSAGE = "command not found"
    NOT_FOUND_MESSAGE = "not found"
    SHELL_BUILTIN_MESSAGE = "a shell builtin"
    BIN_METHOD_MESSAGE = "/bin/"
    SHELL_BUILTIN_COMMAND = [
        "echo",
        "exit",
        "type",
    ]
    BIN_COMMAND = [
        "cat",
    ]

    def __init__(self, func_name: str, args: list):
        """

        :param func_name: The function name to call for the command.
        :param args: The parameters to pass to the function.
        """
        self.func_name = func_name
        self.args = args
        self.paths = os.environ["PATH"].split(":")

    def handle_unknown(self):
        print(f"{self.func_name}: {self.ERROR_MESSAGE}")

    @staticmethod
    def exit(_=None):
        exit()

    @staticmethod
    def echo(*args):
        print(*args)

    def type(self, command):
        command_path = None

        for path_name in self.paths:
            if os.path.isfile("/".join([path_name, command])):
                command_path = "/".join([path_name, command])

        if command in self.SHELL_BUILTIN_COMMAND:
            print(f"{command} is {self.SHELL_BUILTIN_MESSAGE}")
        elif command_path:
            print(f"{command} is {command_path}")
        else:
            print(f"{command}: {self.NOT_FOUND_MESSAGE}")

    def start(self):
        func = getattr(self, self.func_name, None)
        try:
            func(*self.args)
        except TypeError:
            if any(os.path.isfile("/".join([path, self.func_name])) for path in self.paths):
                # Reconstruct the user input.
                command = " ".join([self.func_name, " ".join(self.args)])
                os.system(command)
            else:
                self.handle_unknown()
