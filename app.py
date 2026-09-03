from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_shift")
def add_shift():
    return render_template("add_shift.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/my_shifts")
def my_shifts():
    return render_template("my_shifts.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")
