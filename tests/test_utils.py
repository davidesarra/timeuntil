import datetime as dt

import pendulum

from timeuntil import utils


def test_get_timestamp():
    # given
    date = dt.date(2020, 2, 1)
    time = dt.time(1, 30)
    time_zone = "Europe/London"
    expected = pendulum.datetime(2020, 2, 1, 1, 30, tz="Europe/London")

    # when
    result = utils.get_timestamp(date=date, time=time, time_zone=time_zone)

    # then
    assert result == expected
