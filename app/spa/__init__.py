from flask import Blueprint

blueprint = Blueprint('spa', __name__)

from . import forms, views
