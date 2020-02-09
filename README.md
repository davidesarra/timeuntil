# Time Until

Time Until is a CLI to display how much time is left until a certain timestamp.

## How to run the app

### Docker

- Install Docker
- Launch the app via `make run_docker` (if you have `make` else execute the
  commands in the recipe manually)

### Locally

- Install Poetry
- Create a virtual environment with Python `3.8`
- Activate the environment
- Install requirements via `poetry install`
- Launch the app via `make run_locally` (if you have `make` else execute the
  commands in the recipe manually)

## Development guidelines

The use of Poetry is experimental. There are still some limits when having to
build a container to run the app. Namely a minimal `setup.py` and a full list
of requirements are still needed. In particular, before each commit run
`make update_requirements` which uses Poetry to export the requirements list
used in the container. This step will be automated via git pre-commit hooks.
