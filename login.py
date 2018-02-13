from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from user import User
from passwordhelper import PasswordHelper
from dbhandler import get_user
PH = PasswordHelper()



def loginPage(error=""):
    return render_template("html/login.html", error=error)

def logout():
    logout_user()
    return redirect(url_for("loginPage"))


def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if validateLogin(username, password):
        user = User(username)
        login_user(user)
        return redirect(url_for('home'))
    error = "Invalid User"
    return loginPage(error=error)


def validateLogin(username, password):
    users = get_user(username)
    user = users[0]
    answer = False
    if user and PH.validate_password(password, user['password'].encode('ascii', 'ignore')):
        answer = True
    return answer

if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    app.run(port=5000, debug=True)
