from flask_wtf import FlaskForm, Form
from wtforms import (
    SearchField, SelectField, SelectMultipleField, StringField, 
    SubmitField, BooleanField, ColorField, DateField, 
    DateTimeField, DecimalField, DecimalRangeField, 
    DateTimeLocalField, EmailField, FieldList, FileField, 
    FloatField, IntegerField, IntegerRangeField, MonthField, 
    MultipleFileField, PasswordField, RadioField, TelField, 
    TextAreaField, TimeField, URLField, ValidationError, WeekField
)
from wtforms.validators import (
    DataRequired, AnyOf, MacAddress, InputRequired, EqualTo, Length
)

from ..models import Users, Employee, Client

# class SubmitForm(FlaskForm):
#     """
#     """

class EmployeeForm(FlaskForm):
    """
    """
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_number = TelField('Phone Number', validators=[
        DataRequired(), 
        Length(min=10, max=10, message='This must be 10 digits.')
    ])
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
    phone_number = TelField('Phone Number', validators=[
        DataRequired(), 
        Length(min=10, max=10, message='This must be 10 digits')
    ])
    submit = SubmitField('Save')

    def validate_phone_number(self, field):
        """
        """
        if Users.query.filter_by(phone_number=field.data).first():
            raise ValidationError('This phone number is already registered.')
