import click


@click.group()
def main() -> None:
    pass


@main.command(
    name="until",
    help="Describe how much time is left until a certain timestamp"
)
@click.argument("timestamp", type=click.STRING)
@click.option(
    "-t",
    "--time-zone",
    type=click.STRING,
    help="Time zone associated to the timestamp",
)
def until(timestamp, time_zone) -> None:
    print(timestamp, time_zone)
