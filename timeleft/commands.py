import click
import pendulum

import timeleft


TIMESTAMP_FORMAT = 'YYYY-MM-DD HH'


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
    help=f"Time zone associated to the timestamp ({TIMESTAMP_FORMAT})",
)
def until(timestamp, time_zone) -> None:
    timestamp = pendulum.from_format(timestamp, TIMESTAMP_FORMAT, tz=time_zone)
    timeleft.timeleft.show_time_until(timestamp=timestamp)
