import datetime as dt
import enum

import pendulum


def show_time_until(timestamp: dt.datetime):
    missing_seconds = get_time_until(timestamp, Unit.SECOND)
    print(f"Missing seconds: {missing_seconds:,.0f}")


class Unit(enum.Enum):
    SECOND = 'SECOND'
    HOUR = 'HOUR'


def get_time_until(timestamp: dt.datetime, unit: Unit):
    now = pendulum.now()
    delta = timestamp - now
    if unit == Unit.SECOND:
        return delta.in_seconds()
    elif unit == Unit.MINUTE:
        return delta.in_minutes()
    else:
        raise ValueError('unit must be a valid Unit enumeration')
