from flask_wtf import Form
from wtforms.fields.html5 import DateField, TimeField


class TimestampForm(Form):
    date = DateField('DatePicker', format='%Y-%m-%d')
    time = TimeField('TimePicker', format='%H:%M')
