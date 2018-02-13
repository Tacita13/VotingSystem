from flask import Flask, render_template, request, redirect, url_for
from passwordhelper import PasswordHelper
from dbhandler import get_user, set_user


PH = PasswordHelper()

def validateRegister(username, name, email, password):
    user = {'user_id': 2, 'username': username, 'name': name,
             'last_name': 'B', 'user_type': 'Student', 'password': PH.get_hash(password),
             'email': email, 'student_number': '801-15-9203', 'date_created': '2018-10-28 12:00:10'}

    return set_user(user)


# Stores user info in DB and returns to index.
def register():
    username= request.form.get("username")
    name = request.form.get("name")
    email = request.form.get("email")
    pw1 = request.form.get("password")
    pw2 = request.form.get("password2")
    if not pw1 == pw2:
        return redirect(url_for('loginPage')) #Passwords provided are not equal.
    if get_user(username):
        return redirect(url_for('loginPage')) #User already registered.
    if validateRegister(username, name, email, pw1):
        return redirect(url_for('loginPage')) #User Successfully Registered
    else:
        return redirect(url_for('loginPage')) #Could not register user.

if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    app.run(port=5000, debug=True)