#!/usr/bin/env python3
"""Base flask application"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Defines babel configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_locale() -> str:
    """Retrieves the locale for a web page."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def index() -> str:
    "renders home page"
    return render_template("3-index.html")


if "__name__" == "__main__":
    app.run(host="0.0.0.0", port=5000)
