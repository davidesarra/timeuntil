from flask import Flask
from flask_bootstrap import Bootstrap


timeuntil_app = Flask(__name__)
timeuntil_app.secret_key = "WHAT-A-SECRET"

Bootstrap(timeuntil_app)

import timeuntil.views  # noqa
