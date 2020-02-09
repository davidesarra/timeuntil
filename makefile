run:
	FLASK_APP=timeleft/app.py flask run

test:
	poetry run pytest -vvv .
