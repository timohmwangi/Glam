from flask import Blueprint

blueprint = Blueprint("employee", __name__)

from . import forms, views
