import requests
from flask import Blueprint


api = Blueprint("api", __name__)


@api.route("/")
def get_instructions():
    return """
    <h2>Hi! These are the main endpoints:</h2>
    <ul>
        <li><a href="/hello">/hello</a></li>
        <li><a href="/quote">/quote</a></li>
    </ul>
    """


@api.route("/hello")
def get_hello_world():
    return "Hello World!"


@api.route("/quote")
def get_quote():
    try:
        quote = _get_quote()
        return _format_quote(quote)
    except Exception as e:
        return str(e)


def _get_quote():
    quotes_url = "https://zenquotes.io/api/random"
    response = requests.get(quotes_url)
    if response.status_code == 200:
        return response.json()[0]
    raise Exception("An error ocurred while fetching data")


def _format_quote(quote):
    if _has_exceeded_free_quote(quote):
        return "Quote has exceeded retry again in 30 secs"
    return {"quote": quote["q"], "author": quote["a"]}


def _has_exceeded_free_quote(quote):
    return "Too many requests" in quote["q"]
