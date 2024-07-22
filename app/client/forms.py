from flask_wtf import FlaskForm, Form
from wtforms import (
    SearchField, SelectField, SelectMultipleField, StringField, 
    SubmitField, BooleanField, ColorField, DateField, 
    DateTimeField, DecimalField, DecimalRangeField, 
    DateTimeLocalField, EmailField, FieldList, FileField, 
    FloatField, IntegerField, IntegerRangeField, MonthField, 
    MultipleFileField, PasswordField, RadioField, TelField, 
    TextAreaField, TimeField, URLField, ValidationError, WeekField, FormField
)
from wtforms.validators import (
    DataRequired, AnyOf, MacAddress, InputRequired, EqualTo, Length
)

from ..models import Bookings, ServiceBookings


class BookedServices(Form):
    """
    """
    



class BookAppointmentForm(FlaskForm):
    """
    """
    # class Meta:
    #     model = Bookings

    booked_time = DateTimeField('Reservation Time')
    booked_services = FieldList(FormField(BookedServices),)
