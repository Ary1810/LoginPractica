from flask import Flask, flash, redirect, render_template, request, url_for
from flask_mysqldb import MySQL
from Config import config 
from models.ModelUsers import ModelUsers
from models.entities.users import User

app = Flask(__name__)
db = MySQL(app)

@app.route("/")
def index():
    return redirect("login")

@app.route("/home")
def home():
    return render_template("public/home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        _user = request.form["username"]
        _pass = request.form["password"]
        print(_user)
        print(_pass)
        if _user == "admin" and _pass == "123":
            return redirect(url_for("home"))
        else:
            flash("Acceso rechazado", "danger")
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(debug=True)  # Agrega debug=True para ver errores en la consola