import datetime as dt

from flask import render_template

from timeleft.app import timeleft_app
from timeleft.forms import TimestampForm


@timeleft_app.route('/', methods=['POST', 'GET'])
def home():
    form = TimestampForm()
    if form.validate_on_submit():
        timestamp = dt.datetime.combine(form.date.data, form.time.data)
        return timestamp.strftime('%Y-%m-%d %H:%M')
    return render_template('base.html', title='Time Left', form=form)
