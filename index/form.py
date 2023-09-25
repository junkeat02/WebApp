from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import PasswordField, SubmitField, IntegerField, StringField, RadioField

PASSENGERS = ["Lee", "Thomas", "Bin Tak", "Jin Er", "Han Lin"]


class SignForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = StringField("Password: ", validators=[DataRequired()])
    submit = SubmitField()


class CheckInForm(FlaskForm):
    # passenger = RadioField("Passengers", validators=[DataRequired()])
    passenger1 = RadioField("Passengers", validators=[DataRequired()],
                            choices=[(1, PASSENGERS[0])])
    passenger2 = RadioField("Passengers", validators=[DataRequired()],
                            choices=[(2, PASSENGERS[1])])
    passenger3 = RadioField("Passengers", validators=[DataRequired()],
                            choices=[(3, PASSENGERS[2])])
    passenger4 = RadioField("Passengers", validators=[DataRequired()],
                            choices=[(4, PASSENGERS[3])])
    passenger5 = RadioField("Passengers", validators=[DataRequired()],
                            choices=[(5, PASSENGERS[4])])

    # passenger2 = RadioField(PASSENGERS[1], validators=[DataRequired()])
    # passenger3 = RadioField(PASSENGERS[2], validators=[DataRequired()])
    # passenger4 = RadioField(PASSENGERS[3], validators=[DataRequired()])
    # passenger5 = RadioField(PASSENGERS[4], validators=[DataRequired()])
    submit = SubmitField()
