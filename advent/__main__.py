import sys
import importlib

from advent.api import AdventAPI


def main():
    a = AdventAPI()
    try:
        day_mod = importlib.import_module(f"advent.days.{sys.argv[1]}")
    except ModuleNotFoundError as e:
        print(e.msg)
        return

    solver = day_mod.DaySolver(a)
    solver.run_solve()


if __name__ == "__main__":
    main()
