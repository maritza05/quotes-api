test:
	poetry run pytest tests || pytest tests

start:
	poetry run flask run || flask run

format:
	poetry run black . || python -m black .


