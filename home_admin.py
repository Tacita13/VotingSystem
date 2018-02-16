from flask import Flask, render_template
from flask_login import login_required, LoginManager
from mockdbhelper import MockDBHelper as DBHelper

DB = DBHelper()
# User Account
@login_required
def home_admin():

    g.group_name = "prueba01"
    current_question = get_in_progress_question(g.group_name)
    questions = get_CompletedQuestion(g.group_name)

    current_meeting = DB.get_meeting(g.group_name)
    title = "2fast4u voting"

    return render_template("html/home_admin.html", questions=questions, current_question= current_question, meeting_title=title)

if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    login_manager = LoginManager(app)
    app.run(port=5000, debug=True)