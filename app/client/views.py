from collections import namedtuple
from flask import (
    render_template, flash, url_for, 
    make_response, redirect, request
) 
from flask_cors import cross_origin 
from flask_login import (
    login_required, current_user
)

from . import blueprint
from ..main.forms import BookingsForm, ServiceBookingsForm

from ..models import (
    Bookings, ServiceBookings, Service
)
from ..extensions import csrf

@blueprint.before_request
@login_required
def before_request_handler():
    """
    """
    if current_user.type != 'client':
        return redirect(url_for(f'{current_user.type}.dashboard'))


@blueprint.route('/')
def dashboard():
    """
    """
    # print('current user', current_user, current_user.first_name)
    context = {
        "title": f"{current_user.first_name}'s Dashboard"
    }
    bookings = Bookings.query.filter_by(client_id=current_user.id)
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
    
    # print(sb)

    # x = {
    #     "bookings": [
    #         {
    #             "booking_id": booking.booking_id,
    #             "booked_services": [
    #                 {
    #                     "service": booked_service.service.name
    #                 } for booked_service in booking.service_bookings.all()
    #             ]
    #         } for booking in bookings.all()
    #     ]
    # }
    # print(x)
    context['bookings_count'] = len(Bookings.query.filter_by(client_id=current_user.id).all())
    template = render_template('client/dashboard.html', **context)
    return make_response(template)

# @cross_origin()

@blueprint.route('/book_service', methods=["GET", "POST"]) 
def book_service(): 
    """
    """
    context = {
        "title": "Book a Service."
    }

    print(request.form)
    # get book appointment form
    booking_form = BookingsForm()
    context["booking_form"] = booking_form
    # validate appointment booking on submit
    if booking_form.validate_on_submit():
        print('booking_form')
        booking = Bookings()
        booking_form.populate_obj(booking)
        booking.client_id = current_user.id
        new_booking = booking.save()
        return redirect(url_for('.service_bookings', booking_id=new_booking.id))
    template = render_template('client/book_service.html', **context) 
    return make_response(template)


# @cross_origin(origin='localhost', headers=['Content-Type','application/json'])
@blueprint.route('/booked_service/<booking_id>/add_service_bookings', methods=["GET", "POST"])
@cross_origin()
@csrf.exempt
def service_bookings(booking_id:int):
    """
    """
    context = {
        "title": "Add Services To Your Appointment.",
        "booking_id": booking_id
    }
    booked_service = Bookings.query.get(booking_id)
    services = Service.query.all()
    context["services"] = services
    if request.method.upper() == "POST":
        form_post = request.json.get('selected_services')
        print(form_post)
        for booked_service in form_post:
            service_booking = ServiceBookings()
            # new_service_booking = service_bookings.save()
            if service_booking.create(**booked_service):
                print(service_booking)
        flash('A booking has been reserved for you', "success") 
        return redirect(url_for('.dashboard')) 
    # return a page showing booked appointment with services to book
    booking_service_template = render_template('client/service_bookings.html', **context) 
    return make_response(booking_service_template) 
