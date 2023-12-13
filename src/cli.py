import typer

from day_1 import solution as day_1
from day_2 import solution as day_2
from day_3 import solution as day_3
from day_4 import solution as day_4
from day_5 import solution as day_5
from day_6 import solution as day_6
from day_7 import solution as day_7
from day_8 import solution as day_8
from day_9 import solution as day_9
from day_10 import solution as day_10
from day_11 import solution as day_11
from day_12 import solution as day_12
from day_13 import solution as day_13


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


@app.command()
def day_6a():
    solve = day_6.solution_a()
    typer.echo("Product: " + str(solve))


@app.command()
def day_6b():
    solve = day_6.solution_b()
    typer.echo("Ways to Win: " + str(solve))


@app.command()
def day_7a():
    solve = day_7.solution_a()
    typer.echo("Winnings: " + str(solve))


@app.command()
def day_7b():
    solve = day_7.solution_b()
    typer.echo("Winnings: " + str(solve))


@app.command()
def day_8a():
    solve = day_8.solution_a()
    typer.echo("Path length: " + str(solve))


@app.command()
def day_8b():
    solve = day_8.solution_b()
    typer.echo("Path length: " + str(solve))


@app.command()
def day_9a():
    solve = day_9.solution_a()
    typer.echo("Sum: " + str(solve))


@app.command()
def day_9b():
    solve = day_9.solution_b()
    typer.echo("Sum: " + str(solve))


@app.command()
def day_10a():
    solve = day_10.solution_a()
    typer.echo("Furthest Tile Distance: " + str(solve))


@app.command()
def day_10b():
    solve = day_10.solution_b()
    typer.echo("Inner Tiles: " + str(solve))


@app.command()
def day_11a():
    solve = day_11.solution_a()
    typer.echo("Sum of distances: " + str(solve))


@app.command()
def day_11b():
    solve = day_11.solution_b()
    typer.echo("Sum of distances: " + str(solve))


@app.command()
def day_12a():
    solve = day_12.solution_a()
    typer.echo("Sum: " + str(solve))


@app.command()
def day_12b():
    solve = day_12.solution_b()
    typer.echo("Sum: " + str(solve))


@app.command()
def day_13a():
    solve = day_13.solution_a()
    typer.echo("Summary: " + str(solve))


@app.command()
def day_13b():
    solve = day_13.solution_b()
    typer.echo("Summary: " + str(solve))


if __name__ == "__main__":
    app()