import importlib
import click
from rich import print

from advent.api import AdventAPI


@click.group()
@click.option("--token")
@click.option("--day", "-d")
@click.option("--year", "-y")
@click.pass_context
def cli(ctx, token, day, year):
    ctx.obj = AdventAPI(token=token, year=year, day=day)


@cli.command()
@click.pass_obj
def desc(obj):
    obj.show_description()


@cli.command()
@click.argument("module", required=True)
@click.argument("function")
@click.option("--test", "-t", is_flag=True)
@click.pass_obj
def run(obj, module, function, test):
    try:
        mod = importlib.import_module(module)
    except ModuleNotFoundError as e:
        print(e.msg)
        return

    if function and function in dir(mod):
        if test:
            input = obj.get_test_input()
        else:
            input = obj.get_input()
        res = getattr(mod, function)(input)
        print(
            f"The function [italic red]{function}[/italic red] returns {res}")


if __name__ == "__main__":
    cli()
