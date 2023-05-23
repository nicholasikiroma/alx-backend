#!/usr/bin/env python3
"""Base flask application"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Defines babel configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_user() -> Union[Dict, None]:
    """returns user dictionary"""
    user = request.args.get("login_as")
    if user:
        if int(user) in users:
            return users[int(user)]
        return None
    return None


@app.before_request
def before_request() -> None:
    """executes before other requests"""
    user = get_user()
    g.user = user


def get_locale() -> str:
    """Retrieves the locale for a web page."""
    locale = request.args.get("locale", "")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user["locale"] in app.config["LANGUAGES"]:
        return g.user["locale"]
    header_locale = request.headers.get("locale", "")
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_timezone() -> str:
    """Retrieves the timezone."""
    timezone = request.args.get("timezone", "").strip()
    if not timezone and g.user:
        timezone = g.user["timezone"]
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/")
def index() -> str:
    "renders home page"
    return render_template("7-index.html")


if "__name__" == "__main__":
    app.run(host="0.0.0.0", port=5000)
