from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, form_error
import datetime

# Configure application
app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure SQLite database
db = SQL("sqlite:///sub.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Show for to subscribe to newsletter """
    if request.method == "POST":
        # get form information
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        phone = request.form.get("phone")
        # check for empty field
        if not name or not surname or not email:
            return form_error("Please fill all required field.")
        # insert into database
        if not phone:
            db.execute("INSERT INTO subscribers (name, surname, email) VALUE (?, ?, ?)", name, surname, email)
        else:
            db.execute("INSERT INTO subscribers (name, surname, email, phone) VALUE (?, ?, ?, ?)", name, surname, email, phone)
        flash("Inscription succed!")

        return redirect("/")
    else:
        return render_template("subscribe.html")

@app.route("/count", methods=["GET"])
@login_required
def counter():
    years = db.execute("SELECT DISTINCT year FROM totals ORDER BY year DESC")
    current_year = datetime.now().year
    if current_year in years:
        default_fields = db.execute("SELECT * FROM fields WHERE year = ?", current_year)
    else:
        default_fields = db.execute("SELECT * FROM fields WHERE user_id = ?", session["user_id"])

    return render_template("count.html", available_year=years, default_fields=default_fields)

@app.route("/get-fields")
@login_required
def get_fields():
    year = request.args.get("year")
    fields = db.execute("SELECT * FROM fields WHERE user_id = ?", session["user_id"])
    totals = db.execute("SELECT field_name, total FROM totals WHERE year = ?", year)

    totals_map = {t["field_name"] : t["total"] for t in totals}
    for f in fields:
        f["count"] = totals_map.get(f["name"], 0)
    return {"fields": fields}

@app.route("/update-count", methods=["POST"])
@login_required
def update_count():
    data = request.get_json()
    field_id = data.get("id")
    delta = data.get("delta")
    field = db.execute("SELECT name FROM fields WHERE id = ?", field_id)
    field_name = field[0]["name"]
    if not field:
        return form_error("field does not exist", 400)
    today = datetime.now().date()
    year = today.year
    total = db.execute("SLECT * FROM totals WHERE field_name = ? AND date = ?",field_name, today)
    if total:
        new_count = total[0]["total"] + delta
        db.execute("UPDATE totals SET total = ? WHERE id = ?", new_count, total[0]["id"])
    else:
        new_count = delta
        db.execute("INSERT INTO totals (field_name, date, year, total) VALUES (?, ?, ?, ?)", field_name, today, year, new_count)

    db.execute("INSERT INTO logs (field_name, change) VALUES (?, ?)", field_name, delta)

    return {"sucess": True, "new_count": new_count}

@app.route("/add-field", methods=["POST"])
@login_required
def add_field():
    data = request.get_json()
    name = data.get("name")

    db.execute("INSERT INTO fields (name, user_id) VALUES (?, ?)", name, session["user_id"])
    field = db.execute("SELECT id FROM fields WHERE name = ? AND user_id = ? ORDER BY id DESC LIMIT 1", name, session["user_id"])

    db.execute("INSERT INTO logs (field_name, change) VALUES (?, ?)", name, 0)

    return {"sucess": True, "id": field[0]["id"]}

@app.route("/delete-field", methods=["POST"])
@login_required
def delete_field():
    data = request.get_json()
    field_id = data.get("id")
    field = db.execute("SELECT name FROM fields WHERE id = ?", field_id)

    if not field:
        return form_error("field does not exist", 400)
    field_name = field[0]["name"]
    db.execute("DELETE FROM fields WHERE id = ?", field_id)
    db.execute("INSERT INTO logs (field_name, change) VALUES (?, ?)", field_name, 0)

    return {"sucess" : True}

@app.route("/stat", methods=["GET", "POST"])
@login_required
def stat():
    if request.method == "POST":
        return
    else:
        return render_template("stat.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return form_error("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return form_error("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return form_error("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
