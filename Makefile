.PHONY: docs install test cover format install
all: install cover

build:
	poetry build -f wheel

test:
	poetry run python -m unittest discover tests/

cover:
	poetry run python -m coverage run -m unittest discover tests/
	poetry run python -m coverage report
	poetry run python -m coverage html > /dev/null
	poetry run python -m webbrowser -n file://`pwd`/htmlcov/index.html

format:
	ruff format ./src/

install:
	poetry install
	poetry run pre-commit install

docs:
	cd docs \
	poetry run make html
	poetry run python -m webbrowser -n file://`pwd`/docs/_build/html/index.html
