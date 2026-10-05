import sys
from assistant.rules import reply

def main():
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(reply(query))
        return

    print("Study assistant (starter). Type 'quit' to exit.")
    while True:
        try:
            user_input = input("> ")
        except (EOFError, KeyboardInterrupt):
            break
        if user_input.strip().lower() == "quit":
            break
        print(reply(user_input))

if __name__ == "__main__":
    main()
