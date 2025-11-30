import argparse
import sys
import time
import traceback
from datetime import datetime
from importlib import import_module
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))


def run(func, filename="filename"):
    try:
        with open(filename) as f:
            try:
                start = time.monotonic_ns()
                print(f"{func(f):10d}", end=" ")
                end = time.monotonic_ns()
                print(f"[{(end-start) / 10**6:.3f} ms]")
            except Exception:
                traceback.print_exc()
    except FileNotFoundError:
        print()


if __name__ == "__main__":
    now = datetime.now()
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument(
        "--year", "-y", type=int, help="The year to run.", default=now.year
    )
    parser.add_argument(
        "--day", "-d", type=int, help="The day to run.", default=now.day
    )
    parser.add_argument("--extra", "-e", help="Choose a different solution to run.")
    args = parser.parse_args()

    year_dir = REPO_ROOT / "input" / f"{args.year}"
    if not year_dir.is_dir():
        raise SystemExit(f"Input directory not found: {year_dir}")
    day_prefix = f"day{args.day:02}"
    files = sorted(p for p in year_dir.glob(f"{day_prefix}*.txt"))

    input_paths: dict[str, Path] = {}
    for path in files:
        right = path.name.split(day_prefix, 1)[1]
        if right.startswith("_"):
            input_paths[right[1:].split(".")[0]] = path
        else:
            input_paths["input"] = path

    module_name = f"py.{args.year}.day{args.day:02}"
    if args.extra:
        module_name += f"_{args.extra}"

    print(f"{module_name}")

    module = import_module(module_name)

    for i in ("part1", "part2"):
        if not hasattr(module, i):
            continue

        print(f"{'-'*12} {i} {'-'*12}")
        for name, path in input_paths.items():
            print(f"{name:10s}:", end=" ")
            run(getattr(module, i), path)
