from flask import Flask
from flask_bootstrap import Bootstrap


timeleft_app = Flask(__name__)
timeleft_app.secret_key = 'WHAT-A-SECRET'

Bootstrap(timeleft_app)

import timeleft.views  # noqa
