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

# class SubmitForm(FlaskForm):
#     """
#     """