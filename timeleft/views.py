import flask

from timeleft.app import timeleft_app


@timeleft_app.route('/')
def home():
    return flask.render_template('base.html', title='Time Left')
