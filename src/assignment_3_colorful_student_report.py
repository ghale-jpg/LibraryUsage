

from colorama import Fore, Style, init

PASS_MARK = 40.0
MAX_MARK = 100.0

# autoreset=True restores the default color after every print.
init(autoreset=True)


def read_name() -> str:
   
    while True:
        name = input("Enter the student's name: ").strip()
        if name:
            return name.title()
        print(Fore.YELLOW + "Name cannot be empty.")


def read_marks() -> float:
   
    while True:
        raw = input(f"Enter the marks (0-{MAX_MARK:.0f}): ").strip()
        try:
            marks = float(raw)
        except ValueError:
            print(Fore.YELLOW + "Please enter a valid number.")
            continue
        if 0 <= marks <= MAX_MARK:
            return marks
        print(Fore.YELLOW + f"Marks must be between 0 and {MAX_MARK:.0f}.")


def print_report(name: str, marks: float) -> None:
    
    print("\n" + "=" * 30)
    print(Style.BRIGHT + "STUDENT REPORT")
    print("=" * 30)
    print("Name  : " + Fore.CYAN + name)
    print(f"Marks : {marks:g}")
    if marks >= PASS_MARK:
        print("Result: " + Fore.GREEN + "PASS")
    else:
        print("Result: " + Fore.RED + "FAIL")
    print("=" * 30)


def main() -> None:
    name = read_name()
    marks = read_marks()
    print_report(name, marks)


if __name__ == "__main__":
    main()
