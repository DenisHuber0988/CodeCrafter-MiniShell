class Handler:

    ERROR_MESSAGE = "command not found"
    NOT_FOUND_MESSAGE = "not found"
    SHELL_BUILTIN_MESSAGE = "a shell builtin"
    BIN_METHOD_MESSAGE = "/bin/"
    SHELL_BUILTIN_METHOD = [
        "echo",
        "exit",
        "type",
    ]
    BIN_METHOD = [
        "cat",
    ]

    def __init__(self, func_name, args: list):
        """

        :param func_name: The function name to call for the command.
        :param args: The parameters to pass to the function.
        """
        self.func_name = func_name
        self.args = args

    def handle_unknown(self):
        print(f"{self.func_name}: {self.ERROR_MESSAGE}")

    @staticmethod
    def exit(_):
        exit()

    @staticmethod
    def echo(*args):
        print(*args)

    def type(self, method):
        if method in self.SHELL_BUILTIN_METHOD:
            print(f"{method} is {self.SHELL_BUILTIN_MESSAGE}")
        elif method in self.BIN_METHOD:
            print(f"{method} is {self.BIN_METHOD_MESSAGE}{method}")
        else:
            print(f"{method}: {self.NOT_FOUND_MESSAGE}")

    def start(self):
        func = getattr(self, self.func_name, None)
        try:
            func(*self.args)
        except TypeError:
            self.handle_unknown()
