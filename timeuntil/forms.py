import pendulum
from flask_wtf import Form
from wtforms.fields.core import SelectField
from wtforms.fields.html5 import DateField, TimeField


class TimestampForm(Form):
    date = DateField("DatePicker", format="%Y-%m-%d")
    time = TimeField("TimePicker", format="%H:%M")
    time_zone = SelectField(
        "TimeZonePicker", choices=tuple(zip(pendulum.timezones, pendulum.timezones)),
    )
