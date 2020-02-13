update_requirements:
	poetry export -f requirements.txt > requirements.txt

run_docker:
	docker build -f Dockerfile -t timeuntil . && \
	docker run -it -p 5000:5000 -u 1000:1000 timeuntil

run_locally:
	uwsgi --socket 0.0.0.0:5000 --protocol=http --yaml uwsgi.yaml

test:
	poetry run pytest -vvv .

format:
	black .
