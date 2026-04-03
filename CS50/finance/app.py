import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    id = session["user_id"]
    # get current sum of each share hold by user
    counts = db.execute("""
        SELECT symbol,
            SUM(CASE WHEN type = 'buy' THEN shares
                     WHEN type = 'sell' THEN -shares END
                ) AS shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING shares > 0
    """, id)
    holdings = []
    tHoldings = 0
    for c in counts:
        symbol = c["symbol"]
        shares = c["shares"]

        quote = lookup(symbol)
        if quote is None:
            flash("No information!")
            continue
        price = quote["price"]
        value = shares * price
        tHoldings += value

        holdings.append({"symbol": symbol,
                         "name": quote["name"],
                         "shares": shares,
                         "price": price,
                         "value": value,
                         })

    cash = db.execute("SELECT cash FROM users WHERE id = ?", id)[0]["cash"]
    total = cash + tHoldings
    return render_template("index.html", holdings=holdings, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        sym = request.form.get("symbol")
        shr = request.form.get("shares")
        stock = lookup(sym)

        # check for empty field
        if not sym:
            return apology("Must provide symbol")
        sym = sym.upper()

        if not shr or not shr.isdigit() or int(shr) <= 0:
            return apology("Invalid number of shares")

        if stock is None:
            return apology("Invalid stock symbol")

        shr = int(shr)
        price = stock["price"]
        tCost = price * shr

        user_balance = db.execute("SELECT cash FROM users WHERE id = ?",
                                  session["user_id"])[0]["cash"]
        # check for enought money
        if tCost > user_balance:
            return apology("Not enough funds")
        # update user balance
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", tCost, session["user_id"])
        # update history
        db.execute("""
            INSERT INTO transactions (user_id, symbol, shares, price, type, time)
            VALUES (?, ?, ?, ?, 'buy', CURRENT_TIMESTAMP)
        """, session["user_id"], sym, shr, price)

        flash("Bought!")
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    id = session["user_id"]

    transactions = db.execute(
        "SELECT symbol, shares, price, type, time FROM transactions WHERE user_id = ? ORDER BY time DESC", id)

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        sym = request.form.get("symbol")
        stock = lookup(sym)

        if not sym:
            return apology("Must provide symbol")
        sym = sym.upper()

        if stock is None:
            return apology("No stock provided")

        return render_template("quote.html", stock=stock)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        user = request.form.get("username")
        pwd = request.form.get("password")
        valid = request.form.get("confirmation")
        # check for valid field
        if not user:
            return apology("Must provide Username")
        if not pwd:
            return apology("Must provide Password")
        if pwd != valid:
            return apology("Passwords do not match")
        # generate hash password
        hashpwd = generate_password_hash(pwd)
        # try to insert into db
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", user, hashpwd)
        except ValueError:
            return apology("Username already used")

        # get id and assign a session
        user = db.execute("SELECT id FROM users WHERE username = ?", user)
        session["user_id"] = user[0]["id"]

        flash("Registered!")
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    id = session["user_id"]

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("Must select symbol")

        if not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("Invalid number of shares")
        shares = int(shares)

        rows = db.execute("""
            SELECT SUM(
                CASE WHEN type = 'buy' THEN shares
                     WHEN type = 'sell' THEN -shares END
            ) AS owned
            FROM transactions
            WHERE user_id = ? AND symbol = ?
            GROUP BY symbol
        """, id, symbol)

        owned = rows[0]["owned"] if rows else 0
        if owned < shares:
            return apology("too many shares")

        quote = lookup(symbol)
        if quote is None:
            return apology("Invalid symbol")

        price = quote["price"]
        proceeds = price * shares

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", proceeds, id)
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, type, time) VALUES ( ?,?,?,?, 'sell', CURRENT_TIMESTAMP)", id, symbol, shares, price)
        flash("Sold!")
        return redirect("/")

    symbols = db.execute("""
        SELECT symbol
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING SUM(
                CASE WHEN type = 'buy' THEN shares
                     WHEN type = 'sell' THEN -shares END
            ) > 0
    """, id)
    symbols = [row["symbol"] for row in symbols]

    return render_template("sell.html", symbols=symbols)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """ Allow user to add some cash to account """
    if request.method == "POST":
        amount = request.form.get("amount")
        if not amount or not amount.isdigit() or int(amount) <= 0:
            return apology("Invalid amount")

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", int(amount), session["user_id"])
        flash("Cash added!")
        return redirect("/")
    else:
        return render_template("add_cash.html")


@app.route("/change_pwd", methods=["GET", "POST"])
@login_required
def chg_pwd():
    """ Allow user to change password """
    if request.method == "POST":
        old = request.form.get("old")
        new = request.form.get("new")
        con = request.form.get("confirm")
        if not old or not new or not con:
            return apology("All fields required")

        if new != con:
            return apology("Password do not match")

        hash = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])[0]
        if not check_password_hash(hash["hash"], old):
            return apology("incorrect current password")

        new_hash = generate_password_hash(new)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_hash, session["user_id"])
        flash("Password changed!")
        return redirect("/")
    else:
        return render_template("chg_pwd.html")
