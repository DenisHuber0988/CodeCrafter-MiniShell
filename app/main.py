import sys


# The list of the supported commands.
SUPPORTED_COMMANDS = []

ERROR_MESSAGE = "command not found"


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()
        if command not in SUPPORTED_COMMANDS:
            print(f"{command}: {ERROR_MESSAGE}")


if __name__ == "__main__":
    main()
