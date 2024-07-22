from flask import current_app
from flask_wtf import FlaskForm, Form
from wtforms import (
    SearchField, SelectField, SelectMultipleField, StringField, 
    SubmitField, BooleanField, ColorField, DateField, 
    DateTimeField, DecimalField, DecimalRangeField, 
    DateTimeLocalField, EmailField, FieldList, FileField, FormField,
    FloatField, HiddenField, IntegerField, IntegerRangeField, MonthField, 
    MultipleFileField, PasswordField, RadioField, TelField, 
    TextAreaField, TimeField, URLField, ValidationError, WeekField, widgets
)
from wtforms.validators import (
    DataRequired, AnyOf, MacAddress, InputRequired, EqualTo, Length,
)

from ..models import Users, Service


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class SpaForm(FlaskForm):
    """
    """
    name = StringField('Name', validators=[DataRequired()])
    phone_number = TelField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, message='Password must be at least 8 characters.')])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo(password, 'Passwords must match.')])

    def validate_phone_number(self, field):
        """
        """
        if Users.query.filter_by(phone_number=field.data).first():
            raise ValidationError('This phone number is already registered.')


class EmployeeForm(FlaskForm):
    """
    """
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_number = TelField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, message='Password must be at least 8 characters.')])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo("password", 'Passwords must match.')])
    submit = SubmitField("Add Employee Record")

    def validate_phone_number(self, field):
        """
        """
        if Users.query.filter_by(phone_number=field.data).first():
            raise ValidationError('This phone number is already registered.')


class ClientForm(FlaskForm):
    """
    """
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_number = TelField('Phone Number', validators=[DataRequired(), Length(10, 10, 'This must be 10 digits')])
    password_hash = PasswordField('Password', validators=[DataRequired(), Length(8, message='Password must be at least 8 characters.')])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password_hash', 'Passwords must match.')])
    submit = SubmitField('Save')

    def validate_phone_number(self, field):
        """
        """
        if Users.query.filter_by(phone_number=field.data).first():
            raise ValidationError('This phone number is already registered.')


class ServiceForm(FlaskForm):
    """
    """
    name = StringField('Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])

    def validate_name(self, field):
        """
        """
        if Service.query.filter_by(name=field.data).first():
            raise ValidationError('This service is already registered.')


class ServiceBookingsForm(FlaskForm):
    """
    """
    booking_id = IntegerField('Booking ID', validators=[DataRequired()], render_kw={"class": "visually-hidden"})
    # HiddenField()
    service_id = MultiCheckboxField("Select Services")

    # served_by_id = SelectField('Served By')
    # complete = BooleanField('Complete')
    # submit = SubmitField('Apply')


class BookingsForm(FlaskForm):
    """
    """
    booking_time = DateTimeField('', validators=[DataRequired()], format="%d.%m.%Y %H:%M")
    booked_services = FieldList(FormField(ServiceBookingsForm))
    submit = SubmitField('Book Session')




class TestimonialsForm(FlaskForm):
    """
    """
    testimonial = TextAreaField("What do you have to say about your service?", validators=[DataRequired()])
    submit = SubmitField('Submit Testimonial')


