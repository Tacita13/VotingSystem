from flask import Flask, render_template
from flask_login import login_required, LoginManager
from mockdbhelper import MockDBHelper as DBHelper

DB = DBHelper()
# User Account
@login_required
def home():
    meetings = DB.get_meetings()
    return render_template("home.html", meetings=meetings)

if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    login_manager = LoginManager(app)
    app.run(port=5000, debug=True)