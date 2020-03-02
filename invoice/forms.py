from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired,  ValidationError


from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms.fields import DateField
from datetime import date
from invoice import db
	
class InvoiceForm(FlaskForm):
    cust_name = StringField('Customer Name', validators=[DataRequired()])
    date_created = DateField('Date', format="%m/%d/%Y")
    submit = SubmitField('Create')

	
class InvoiceItemForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Create')
	