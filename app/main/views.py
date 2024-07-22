from flask import (
    render_template, abort, flash, url_for, 
    current_app, get_flashed_messages, send_file, 
    send_from_directory, jsonify, make_response, 
    redirect, request, session
)
from flask_login import (
    login_required, current_user
)

from . import blueprint
# from .forms import LoginForm
from ..models import Users, Employee, Service, Testimonial


@blueprint.before_request
def before_request():
    """
    """
    if current_user.is_authenticated:
        return redirect(url_for(f'{current_user.type}.dashboard'))


@blueprint.route('/')
def home():
    """
    """
    context = {
        "title": "Home", 
        "employee_list": Employee.query.all(), 
        "services": Service.query.all(),
        "testimonials": Testimonial.query.all()
    }
    template = render_template('index.html', **context)
    return make_response(template)


@blueprint.route('/contact')
def contact():
    """
    """
    context = {
        "title": "Contact"
    }
    template = render_template('contact.html', **context)
    return make_response(template)


@blueprint.route('/about_us')
def about():
    """
    """
    context = {
        "title": "About Us"
    }
    template = render_template('about.html', **context)
    return make_response(template)


@blueprint.route('/appointment')
def appointment():
    """
    """
    context = {
        "title": "Appointment"
    }
    template = render_template('appointment.html', **context)
    return make_response(template)


@blueprint.route('/pricing')
def price():
    """
    """
    context = {
        "title": "Pricing"
    }
    template = render_template('price.html', **context)
    return make_response(template)


@blueprint.route('/services')
def service():
    """
    """
    context = {
        "title": "Services",
        "services": Service.query.all()
    }
    template = render_template('service.html', **context)
    return make_response(template)

@blueprint.route('/team')
def team():
    """
    """
    context = {
        "title": "Team"
    }
    template = render_template('team.html', **context)
    return make_response(template)


@blueprint.route('/opening')
def opening():
    """
    """
    context = {
        "title": "Opening"
    }
    template = render_template('opening.html', **context)
    return make_response(template)

@blueprint.route('/testimonials')
def testimonial():
    """
    """
    context = {
        "title": "Testimonials"
    }
    template = render_template('testimonial.html', **context)
    return make_response(template)
