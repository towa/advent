# Automatically get inputs from AOC and check solutions
import os
from datetime import date

import requests
from markdownify import markdownify
from rich.console import Console
from rich.markdown import Markdown
from rich import print
from lxml import etree


class AdventAPI():
    def __init__(self, token=None, day=None, year=None):
        if not token:
            token = os.environ.get('AOC_TOKEN')
        if not year:
            year = date.today().year
        if not day:
            day = (date.today() - date.fromisoformat(f"{year}-11-30")).days
        self.session_cookie = {'session': token}
        self.base_url = f"https://adventofcode.com/{year}/day/{day}"
        self.day = day
        self.year = year

    def get_input(self):
        res = requests.get(
            f"{self.base_url}/input",
            cookies=self.session_cookie
        )
        return res.content.decode().splitlines()
    
    def get_test_input(self):
        res = requests.get(
            self.base_url,
            cookies=self.session_cookie
        )
        root = etree.HTML(res.content.decode())
        code = root.xpath("//pre/code")
        if code:
            return code[0].text.splitlines()
        else:
            return None

    def post_answer(self, level, answer):
        payload = {'level': level, 'answer': answer}
        res = requests.post(
            f"{self.base_url}/answer",
            data=payload, cookies=self.session_cookie)
        print(res.content)

    def show_description(self):
        res = requests.get(
            self.base_url,
            cookies=self.session_cookie
        )
        console = Console()
        html_str = res.content.decode()
        root = etree.HTML(html_str)
        article = root.xpath('//article')
        if article:
            md = Markdown(markdownify(etree.tostring(article[0])))
            console.print(md)
        else:
            print(f"[bold]No entry for year {self.year} day {self.day}")
