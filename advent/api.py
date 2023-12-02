# Automatically get inputs from AOC and check solutions
import requests
import os


class AdventAPI():
    def __init__(self, token=None, year=2023):
        if not token:
            token = os.environ.get('AOC_TOKEN')
        self.session_cookie = {'session': token}
        self.base_url = f"https://adventofcode.com/{year}"
        self.year = year

    def get_input(self, day):
        res = requests.get(
            f"{self.base_url}/day/{day}/input",
            cookies=self.session_cookie
        )
        return res.content.decode().splitlines()

    def post_answer(self, day, level, answer):
        payload = {'level': level, 'answer': answer}
        res = requests.post(
            f"{self.base_url}/day/{day}/answer",
            data=payload, cookies=self.session_cookie)
        print(res.content)
