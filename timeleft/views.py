import datetime as dt

import pendulum
from flask import render_template

from timeleft.app import timeleft_app
from timeleft.forms import TimestampForm


@timeleft_app.route('/', methods=['POST', 'GET'])
def home():
    form = TimestampForm()
    if form.validate_on_submit():
        timestamp = dt.datetime.combine(form.date.data, form.time.data)
        time_zone = form.time_zone.data
        tz_timestamp = pendulum.instance(timestamp, tz=time_zone)
        return str(tz_timestamp)
    return render_template('base.html', title='Time Left', form=form)
