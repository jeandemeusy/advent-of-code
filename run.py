import argparse
import os
import time
import traceback
from datetime import datetime
from importlib import import_module


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

    files = [
        f"input/{args.year}/{f}"
        for f in os.listdir(f"./input/{args.year}/")
        if f.startswith(f"day{args.day:02}")
    ]
    files = sorted(files)

    input_paths = {}
    for f in files:
        right = f.split(f"day{args.day:02}")[1]
        if right.startswith("_"):
            input_paths[right[1:].split(".")[0]] = f
        else:
            input_paths["input"] = f

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
