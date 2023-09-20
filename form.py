from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import PasswordField, SubmitField, IntegerField, StringField, RadioField

PASSENGERS = ["Lee", "Thomas", "Bin Tak", "Jin Er", "Han Lin"]


class SignForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = StringField("Password: ", validators=[DataRequired()])


class CheckInForm(FlaskForm):
    passengers = RadioField("Passengers", validators=[DataRequired()], choices=[x for x in PASSENGERS[:1]])
    # passenger2 = RadioField(PASSENGERS[1], validators=[DataRequired()])
    # passenger3 = RadioField(PASSENGERS[2], validators=[DataRequired()])
    # passenger4 = RadioField(PASSENGERS[3], validators=[DataRequired()])
    # passenger5 = RadioField(PASSENGERS[4], validators=[DataRequired()])
    submit = SubmitField()

