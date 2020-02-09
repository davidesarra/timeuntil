update_requirements:
	poetry export -f requirements.txt > requirements.txt

run_docker:
	docker build -f Dockerfile -t timeuntil . && \
	docker run -it -p 5000:5000 timeuntil

run_locally:
	FLASK_APP=timeuntil/app.py flask run

test:
	poetry run pytest -vvv .
