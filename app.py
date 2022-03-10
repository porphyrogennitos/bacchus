import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///bacchus.db")


@app.route("/")
@login_required
def index():
    """Show festivals"""

    # Get festivals table
    festivals = db.execute("SELECT * FROM festivals")

    return render_template("index.html", festivals=festivals)


@app.route("/header")
def header():
    return render_template("header.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login user."""

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Ensure email was submitted
        if not email:
            return apology("Πρέπει να συμπληρώσεις το email.")

        # Ensure password was submitted
        elif not password:
            return apology("Πρέπει να συμπληρώσεις τον κωδικό.")

        rows = db.execute("SELECT * FROM users WHERE email = ?", email)

        # Ensure email exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("Λανθασμένο email ή κωδικός.", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out."""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Ensure email is not blank
        if not email:
            return apology("Πρέπει να συμπληρώσεις το email.")

        # Ensure password is not blank
        if not password:
            return apology("Πρέπει να συμπληρώσεις τον κωδικό.")

        # Ensure email doesn't exist
        rows = db.execute("SELECT * FROM users WHERE email = ?", email)
        if len(rows) == 1:
            return apology("Ο χρήστης υπάρχει ήδη!")

        # Add user
        db.execute("INSERT INTO users (email, hash) VALUES(?, ?)",
                   email, generate_password_hash(password))

        return redirect("/")
    else:
        return render_template("register.html")
