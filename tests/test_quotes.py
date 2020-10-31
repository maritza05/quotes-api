import json
import requests
from unittest.mock import patch, MagicMock


def test_get_hello_world(client):
    response = client.get("/hello")
    assert _get_as_text(response) == "Hello World!"


@patch.object(requests, "get")
def test_get_quote_with_valid_response(mock_get_quote, client):
    author = "me"
    quote = "This is a quote"
    mock_response = _given_valid_response(author=author, quote=quote)
    mock_get_quote.return_value = mock_response

    response = client.get("/quote")
    data = _get_as_json(response)

    assert data["author"] == author
    assert data["quote"] == quote


@patch.object(requests, "get")
def test_get_quote_with_error_as_response(mock_get_quote, client):
    mock_response = _given_error_response()
    mock_get_quote.return_value = mock_response

    response = client.get("/quote")

    assert _get_as_text(response) == "An error ocurred while fetching data"


@patch.object(requests, "get")
def test_get_quote_with_exceeded_requests_response(mock_get_quote, client):
    author = "ZenQuotes.io"
    quote = "Too many requests. Obtain an auth key for unlimited access."
    mock_response = _given_valid_response(author=author, quote=quote)
    mock_get_quote.return_value = mock_response

    response = client.get("/quote")

    assert _get_as_text(response) == "Quote has exceeded retry again in 30 secs"


def _given_valid_response(author, quote):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json = MagicMock(return_value=[{"q": quote, "a": author}])
    return mock_response


def _given_error_response():
    mock_response = MagicMock()
    mock_response.status_code = 500
    return mock_response


def _get_as_json(response):
    return json.loads(response.data)


def _get_as_text(response):
    return response.data.decode("utf-8")
