run:
	FLASK_APP=timeuntil/app.py flask run

test:
	poetry run pytest -vvv .
