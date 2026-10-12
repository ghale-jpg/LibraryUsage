

import pyjokes

INITIAL_JOKE_COUNT = 3
YES_ANSWERS = {"yes", "y"}
NO_ANSWERS = {"no", "n"}


def show_joke() -> None:
    
    print(f"  -> {pyjokes.get_joke(language='en', category='neutral')}")


def ask_yes_no(prompt: str) -> bool:
    
    while True:
        answer = input(prompt).strip().lower()
        if answer in YES_ANSWERS:
            return True
        if answer in NO_ANSWERS:
            return False
        print("Please answer 'yes' or 'no'.")


def main() -> None:
    print("Here are some programming jokes:\n")
    for number in range(1, INITIAL_JOKE_COUNT + 1):
        print(f"Joke {number}:")
        show_joke()

    while ask_yes_no("\nWould you like another joke? (yes/no): "):
        show_joke()

    print("\nThanks for laughing along. Happy coding!")


if __name__ == "__main__":
    main()
