from flask import Flask, render_template
from mockdbhelper import MockDBHelper as DBHelper
from passwordhelper import PasswordHelper

PH = PasswordHelper()
DB = DBHelper()


def index():
    return render_template("html/mainpage.html")

if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    app.run(port=5000, debug=True)

