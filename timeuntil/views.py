from flask import render_template

from timeuntil.app import timeuntil_app
from timeuntil.forms import TimestampForm
from timeuntil.utils import get_timestamp


@timeuntil_app.route("/", methods=["POST", "GET"])
def home():
    title = "Time Until"
    template_name = "base.html"
    form = TimestampForm()
    if form.validate_on_submit():
        timestamp = get_timestamp(
            date=form.date.data, time=form.time.data, time_zone=form.time_zone.data
        )
        return render_template(
            template_name, title=title, form=form, timestamp=timestamp
        )
    return render_template(template_name, title=title, form=form)
