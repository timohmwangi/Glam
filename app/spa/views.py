from flask import (
    render_template, abort, flash, url_for,
    current_app, get_flashed_messages, send_file,
    send_from_directory, jsonify, make_response,
    redirect, request, session
)
from flask_login import (
    current_user, login_required
)

from . import blueprint
# from .forms import LoginForm
from ..extensions import login_manager
from ..models import (
    Users, Bookings, Employee, Client
)
from .forms import EmployeeForm, ClientForm
# from ..main.forms import EmployeeForm

@login_required
@blueprint.before_request
def before_request():
    """
    """
    if current_user.is_authenticated and current_user.type != 'spa':
        return redirect(url_for(f'{current_user.type}.dashboard'))


# @login_required
@blueprint.route('/')
def dashboard():
    """
    """
    context = {
        "title": " Dashboard.",
        "employee_list": Employee.query,
        "client_list": Client.query
    }

    bookings = Bookings.query
    # print(bookings)
    # print(dir(bookings))
    # context['bookings'] = bookings
    sb = {
        "bookings_count": bookings.count(), 
        "booked_services": []
    }
    for booking in bookings.all():
        booking_data = {
            "booking_id": booking.id, 
            "booking_time": booking.booking_time, 
            "services_count": booking.service_bookings.count(),
            "booking_cost": sum([
                b.service.price for b in booking.service_bookings.all()
            ])
        }
        booked_services = booking.service_bookings.all()
        ls = []
        for booked_service in booked_services:
            # if booked_service:
            print(booked_service)
            ls.append({
                "service": booked_service.service, 
                # "served_by": booked_service.served_by.first_name

            })
        booking_data["booked_services"] = ls
        sb["booked_services"].append(booking_data)
    context["bookings"] = sb
    template = render_template('spa/dashboard.html', **context)
    return make_response(template)

@blueprint.route('/add_employee', methods=["GET", "POST"])
def add_employee():
    """
    """
    context = {
        "title": "Add Employee"
    }
    employee_form = EmployeeForm()
    context["form"] = employee_form
    if employee_form.validate_on_submit():
        employee = Employee()
        employee_form.populate_obj(employee)
        employee.set_password(employee_form.phone_number.data)
        new_employee = employee.save()
        flash(f'Successfully added Employee {new_employee.first_name}!', "success")
        return redirect(url_for('spa.dashboard'))
    template = render_template('spa/add_employee.html', **context)
    return make_response(template)

@blueprint.route('/add_client', methods=["GET", "POST"])
def add_client():
    """
    """
    context = {
        "title": "Add Client"
    }
    client_form = ClientForm()
    context["form"] = client_form
    if client_form.validate_on_submit():
        client = Client()
        client_form.populate_obj(client)
        client.set_password(client_form.phone_number.data)
        new_client = client.save()
        flash(f'Successfully added client {new_client.first_name}!', "success")
        return redirect(url_for('spa.dashboard'))
    template = render_template('spa/add_client.html', **context)
    return make_response(template)
