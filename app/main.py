import sys


# The list of the supported commands.
SUPPORTED_COMMANDS = [
    "exit",
]

ERROR_MESSAGE = "command not found"


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = input().split()
        command = user_input.pop(0)
        args = user_input

        if command not in SUPPORTED_COMMANDS:
            print(f"{command}: {ERROR_MESSAGE}")
        else:
            func = getattr(sys, command)
            func()


if __name__ == "__main__":
    main()
