# Time Until

Time Until is a Flask web app to count down to any date and time in any time
zone.

## How to run the app

### Docker

- Install [Docker](https://www.docker.com/)
- Launch the app via `make run_docker`

### Locally

- Install [Poetry](https://python-poetry.org/)
- Install [Yarn](https://yarnpkg.com/)
- Create a virtual environment with Python `3.8`
- Activate the virtual environment
- Install the app via `make install_locally`
- Launch the app via `make run_locally`

## Development guidelines

The use of Poetry is experimental. There are still some limits when having to
build a container to run the app. Namely a minimal `setup.py` and a full list
of requirements are still needed. In particular, before each commit run
`make update_requirements` which uses Poetry to export the requirements list
used in the container. This step will be automated via git pre-commit hooks.
