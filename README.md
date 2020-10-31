## Quotes API

This is a basic REST api that provides two endpoints:
* [hello](http://localhost:5000/hello): A simple endpoint that displays "Hello World!"
* [quote](http://localhost:5000/quote): A endpoint that get's inspirational quotes from the [zenquotes](https://zenquotes.io/#docs) API.

### Structure and Organization
The principal structure of the project is the following:
```
.
├── Makefile               # Commands to run the app
├── app.py                 # Application entrypoint
├── pyproject.toml         # Poetry dependencies
├── requirements.txt       # Alternative pip dependencies 
├── quotes
│   └── routes.py          # Endpoints definition 
└── tests
    ├── conftest.py        # Test fixtures and setup
    └── test_quotes.py     # Tests
```


### Built With
This API was created with in the Python language and with the following tools:
* [Flask](https://flask.palletsprojects.com/en/1.1.x/): As web framework.
* [Pytest](https://docs.pytest.org/en/stable/): As library used to setup the tests.
* [Pytest-Flask](https://github.com/pytest-dev/pytest-flask): Package to handle tests in the flask framework. 
* [Poetry](https://python-poetry.org/): Tool for dependency management and packaging.

### Installation and Dependencies
1. The project uses [poetry](https://python-poetry.org/) to handle the dependencies. Poetry is similar to npm but for Python. To install poetry you can run the following command on osx / linux / bashonwindows:
   
   ```curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -```

   For instructions or further details you can check the poetry installation instructions [here](https://python-poetry.org/docs/#installation)

   **As an alternative there's a requirements.txt file, so you can install the dependencies directly with pip without the need to install poetry.**

2. To install the dependencies with poetry run:
   
   `poetry install`

   To install the dependencies with pip run:

   `pip install -r requirements.txt`

### Usage
- To run the project use the following command:

   `make start`

   And in the API should be running in: 
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

- To run the tests use:
  
   `make test`




    
