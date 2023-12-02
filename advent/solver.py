from advent.api import AdventAPI


class Solver():
    day = 1

    def __init__(self, api: AdventAPI) -> None:
        self.api = api

    def solve_1(self, input):
        return 42

    def solve_2(self, input):
        return 42

    def run_solve(self):
        input = self.api.get_input(self.day)
        answer_1 = self.solve_1(input)
        answer_2 = self.solve_2(input)
        print((
            f"The answer for part 1 is {answer_1}. "
            f"The answer for part 2 is: {answer_2}"
        ))
