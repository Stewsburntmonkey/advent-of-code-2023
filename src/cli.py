import typer

from day_1 import solution as day_1
from day_2 import solution as day_2

app = typer.Typer()


@app.command()
def day_1a():
    solve = day_1.solution_a()
    typer.echo("Calibration is " + str(solve))


@app.command()
def day_1b():
    solve = day_1.solution_b()
    typer.echo("Calibration is " + str(solve))


@app.command()
def day_2a():
    solve = day_2.solution_a()
    typer.echo("Sum is " + str(solve))


@app.command()
def day_2b():
    solve = day_2.solution_b()
    typer.echo("Sum of game powers is " + str(solve))


if __name__ == "__main__":
    app()