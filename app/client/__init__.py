from flask import Blueprint

blueprint = Blueprint("client", __name__)

from . import forms, views
