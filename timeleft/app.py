from flask import Flask

timeleft_app = Flask(__name__)

import timeleft.views  # noqa
