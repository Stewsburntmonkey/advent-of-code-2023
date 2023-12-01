import typer

from day_1.solution import solution_a, solution_b

app = typer.Typer()


@app.command()
def day_1a():
    solve = solution_a()
    typer.echo("Calibration is " + str(solve))


@app.command()
def day_1b():
    solve = solution_b()
    typer.echo("Calibration is " + str(solve))


if __name__ == "__main__":
    app()