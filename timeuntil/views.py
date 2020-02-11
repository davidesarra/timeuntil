import datetime as dt

import pendulum
from flask import render_template

from timeuntil.app import timeuntil_app
from timeuntil.forms import TimestampForm


@timeuntil_app.route("/", methods=["POST", "GET"])
def home():
    title = "Time Until"
    template_name = "base.html"
    form = TimestampForm()
    if form.validate_on_submit():
        timestamp = dt.datetime.combine(form.date.data, form.time.data)
        time_zone = form.time_zone.data
        tz_timestamp = pendulum.instance(timestamp, tz=time_zone)
        return render_template(
            template_name, title=title, form=form, timestamp=tz_timestamp
        )
    return render_template(template_name, title=title, form=form)
