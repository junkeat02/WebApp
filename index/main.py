from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_bootstrap import Bootstrap
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, LoginManager, current_user, login_user, logout_user, UserMixin

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///checkin.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

PASSENGERS = ["Lee", "Thomas", "Bin Tak", "Jin Er", "Han Lin"]


class User(UserMixin, db.Model):
    __tablename__ = "Car_users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(250), nullable=True)
    check_list = relationship("CheckList", back_populates="user")

class CheckList(db.Model):
    __tablename__ = "Check_in_list"
    id = db.Column(db.Integer, primary_key=True)
    Lee = db.Column(db.Integer, nullable=True)
    Thomas = db.Column(db.Integer, nullable=True)
    Bin_Tak = db.Column(db.Integer, nullable=True)
    Han_Lin = db.Column(db.Integer, nullable=True)
    Jin_Er = db.Column(db.Integer, nullable=True)
    others = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=True)
    date = db.Column(db.String(250), nullable=True)
    time = db.Column(db.String(250), nullable=True)
    who_check_in = db.Column(db.Integer, db.ForeignKey("Car_users.id"), nullable=True)
    user = relationship("User", back_populates="check_list")


with app.app_context():
    db.create_all()


def say_greeting():
    hours = int(datetime.now().strftime("%H"))
    if 12 >= hours >= 0:
        greeting = "Good morning!"
    elif 18 > hours > 12:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    return greeting


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username)
        user = User.query.filter_by(name=username).first()
        print(user)
        if user:
            if check_password_hash(user.password, password):
                print("hello")
                login_user(user)
                return redirect(url_for("check_in"))
            else:
                flash("Password and username doesn't match")
        else:
            flash("You have not register")
            return redirect(url_for("access"))

    greeting = say_greeting()

    return render_template("index.html", greeting=greeting)


@app.route("/access", methods=["GET", "POST"])
def access():
    if request.method == "POST":
        code = "6566"
        if request.form["code"] == code:
            return redirect(url_for("register"))
        else:
            return redirect(url_for("access"))

    return render_template("access.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password = generate_password_hash(password, "pbkdf2:sha256")
        new_user = User(
            name=username,
            password=password,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("check_in"))
    return render_template("register.html")


@app.route("/check-in", methods=["POST", "GET"])
@login_required
def check_in():
    if request.form:
        now = datetime.now()
        new_data_dict = {key: value for (key, value) in request.form.items()}
        for passenger in PASSENGERS:
            if passenger not in new_data_dict:
                new_data_dict[passenger] = 0
        new_data = CheckList(
            Lee=new_data_dict["Lee"],
            Thomas=new_data_dict["Thomas"],
            Bin_Tak=new_data_dict["Bin Tak"],
            Han_Lin=new_data_dict["Han Lin"],
            Jin_Er=new_data_dict["Jin Er"],
            date=now.strftime("%Y-%m-%d"),
            time=now.strftime("%H:%M:%S"),
            location=new_data_dict["location"],
            others=new_data_dict["others"],
            user=current_user
        )
        db.session.add(new_data)
        db.session.commit()
        # print(now.strftime("%Y-%m-%d"))
        # print(now.strftime("%H:%M:%S"))
        # print(new_data_dict)
        return redirect(url_for("check_in"))
    return render_template("check_in.html", name_list=PASSENGERS)


if __name__ == "__main__":
    app.run()
