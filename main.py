from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from form import CheckInForm, SignForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route("/")
def home():
    form = SignForm()
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=81)
