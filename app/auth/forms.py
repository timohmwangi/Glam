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
    DataRequired, AnyOf, MacAddress, InputRequired, EqualTo, Length, NumberRange
)

from ..models import Users

class LoginForm(FlaskForm):
    """
    """
    phone_number = TelField("Phone Number", validators=[DataRequired(), Length(10, 10)])
    password = PasswordField("Password", validators=[DataRequired(), Length(8)])
    remember_me = BooleanField("Keep me logged in.")
    submit = SubmitField("Login")

    def validate_phone_number(self, field):
        """
        """
        if not Users.query.filter_by(phone_number=field.data).first():
            raise ValidationError('User does not exist!')


