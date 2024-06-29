import sys


# The list of the supported commands.
SUPPORTED_COMMANDS = {
    "exit": "handle_exit",
    "echo": "handle_echo",
}


ERROR_MESSAGE = "command not found"


def handle_exit(_):
    exit()


def handle_echo(*args):
    print(*args)


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = input().split()
        try:
            command = user_input.pop(0)
        except ValueError:
            break

        args = user_input

        if command not in SUPPORTED_COMMANDS.keys():
            print(f"{command}: {ERROR_MESSAGE}")
        else:
            func_name = SUPPORTED_COMMANDS[command]
            func = globals()[func_name]
            func(*args)


if __name__ == "__main__":
    main()
