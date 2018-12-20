from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, SelectMultipleField, SelectField ,validators
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from .models import Todolist




class TestModelForm(Form):
    content = StringField('content', [validators.Length(min=1, max=50,message='content必须介于1-50字符！')])
    title = StringField('title', validators=[DataRequired(),Length(min=1, max=10, message='title必须介于1-10字符！')])
    date = DateField('date', validators=[DataRequired()])


