from flask import Flask
from flask_bootstrap import Bootstrap


timeleft_app = Flask(__name__)
Bootstrap(timeleft_app)

import timeleft.views  # noqa
