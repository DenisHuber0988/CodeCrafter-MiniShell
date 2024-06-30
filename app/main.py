import sys

from app.handler import Handler


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = input().split()
        try:
            command = user_input.pop(0)
            args = user_input
            handler = Handler(func_name=command, args=args)
            handler.start()
        except IndexError:
            break


if __name__ == "__main__":
    main()
