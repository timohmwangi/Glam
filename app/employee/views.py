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
from ..extensions import csrf
from ..models import (
    Users, Employee, ServiceBookings
)

@blueprint.before_request
@login_required
def before_request():
    """
    """
    if current_user.type != 'employee':
        return redirect(url_for(f'{current_user.type}.dashboard'))


@blueprint.route('/')
@login_required
def dashboard():
    """
    """
    context = {
        "title": f"{current_user.first_name.title} Dashboard."
    }
    work_load = ServiceBookings.query.filter_by(served_by_id=current_user.id, complete=False)
    context["work_load"] = [
        {
            "booking": work.booking,
            "client": work.booking.client,
            "service": work.service,
            "work": work,
        } for work in work_load
    ]
    
    print(context["work_load"])
    template = render_template('employee/dashboard.html', **context)
    return make_response(template)

@blueprint.route('/complete_job/<int:booking_id>/<int:service_id>', methods=["PUT"])
@csrf.exempt
def complete_job(booking_id:int, service_id:int):
    """
    """
    job = ServiceBookings.query.filter_by(booking_id=booking_id, service_id=service_id, served_by_id=current_user.id).first()
    job.update(complete=True)
    return make_response({"completed": job.complete}), 201
