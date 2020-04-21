install_locally:
	pip install --upgrade pip && \
	poetry install && \
	cd timeuntil/static/js && \
	yarn install && \
	cd ../../..

run_docker:
	docker build -f Dockerfile -t timeuntil . && \
	docker run -it -p 5000:5000 -u 1000:1000 timeuntil

run_locally:
	uwsgi --socket 0.0.0.0:5000 --protocol=http --yaml uwsgi.yaml

test:
	black --diff --check . && \
	flake8 && \
	poetry run pytest -vvv .

format:
	black .
