from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from user import User
from passwordhelper import PasswordHelper
from dbhandler import get_user, get_user_type, has_permission
PH = PasswordHelper()



def loginPage(error=""):
    return render_template("html/login.html", error=error)

def logout():
    logout_user()
    return redirect(url_for("loginPage"))


def login():
    group_name = "prueba01"
    username = request.form.get("username")
    password = request.form.get("password")
    error = "Invalid User"
    print("Validating User")
    if validateLogin(username, password):
        print("User Valid")
        user = User(username)
        login_user(user)
        user_type = get_user_type(username)
        print("user_type: %s %s" % (user_type, type(user_type)))
        if user_type is None:
            return loginPage(error="Invalid User")
        elif user_type['user_type'] == "Staff":
            return redirect(url_for('home_admin'))
        else:
            permission = has_permission(username, group_name)
            if len(permission):
                return redirect(url_for('home'))
            else:
                logout_user()
                error = "Access Denied"
    print("Invalid User")
    return loginPage(error=error)


def validateLogin(username, password):
    print("Identifier: Level1_Item01")
    print("Type: Unit Test (Black Box)")
    print("Input: username: %s, password: %s " % (username, password))
    users = get_user(username)
    answer = False
    if users:
        user = users.pop()
        print("user: %s" % user)
        print("pass: %s" % password)
        if user and PH.validate_password(password, user['password']):
            answer = True
    print("Output: %s")
    return answer

if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    app.run(port=5000, debug=True)
