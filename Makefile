get-pipenv:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

test:
	poetry run pytest tests || pytest tests

start:
	poetry run flask run || flask run

format:
	poetry run black . || python -m black .


