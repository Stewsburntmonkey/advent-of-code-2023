import typer

from day_1 import solution as day_1
from day_2 import solution as day_2
from day_3 import solution as day_3
from day_4 import solution as day_4
from day_5 import solution as day_5

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


@app.command()
def day_3a():
    solve = day_3.solution_a()
    typer.echo("Sum is " + str(solve))


@app.command()
def day_3b():
    solve = day_3.solution_b()
    typer.echo("Sum of rations is " + str(solve))


@app.command()
def day_4a():
    solve = day_4.solution_a()
    typer.echo("Winning Points: " + str(solve))


@app.command()
def day_4b():
    solve = day_4.solution_b()
    typer.echo("Total Cards: " + str(solve))


@app.command()
def day_5a():
    solve = day_5.solution_a()
    typer.echo("Miminum location: " + str(solve))


@app.command()
def day_5b():
    solve = day_5.solution_b()
    typer.echo("Miminum location: " + str(solve))


if __name__ == "__main__":
    app()