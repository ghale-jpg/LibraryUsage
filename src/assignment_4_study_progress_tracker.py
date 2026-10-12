
import argparse
import time

from tqdm import tqdm

TOTAL_TASKS = 20
DEFAULT_DELAY = 0.3  # seconds per task


def positive_float(value: str) -> float:
    
    number = float(value)
    if number < 0:
        raise argparse.ArgumentTypeError("delay must not be negative")
    return number


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Study progress tracker")
    parser.add_argument(
        "--delay",
        type=positive_float,
        default=DEFAULT_DELAY,
        help=f"seconds per task (default: {DEFAULT_DELAY}); smaller is faster",
    )
    parser.add_argument(
        "--desc",
        default="Studying Python",
        help="text shown beside the progress bar",
    )
    return parser.parse_args()


def run_tasks(description: str, delay: float) -> None:
    
    for _ in tqdm(range(TOTAL_TASKS), desc=description, unit="task"):
        time.sleep(delay)  # stands in for real work


def main() -> None:
    args = parse_args()
    run_tasks(args.desc, args.delay)
    print(f"All {TOTAL_TASKS} tasks completed. Great work!")


if __name__ == "__main__":
    main()
