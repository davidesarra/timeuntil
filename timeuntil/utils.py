import datetime as dt

import pendulum


def get_timestamp(date: dt.date, time: dt.time, time_zone: str) -> pendulum.datetime:
    timestamp = dt.datetime.combine(date, time)
    return pendulum.instance(timestamp, tz=time_zone)
