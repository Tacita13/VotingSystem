from flask import Flask, render_template
from flask_login import login_required, LoginManager
from mockdbhelper import MockDBHelper as DBHelper

DB = DBHelper()
# User Account
@login_required
def home():
    meeting_id = 1
    questions = DB.get_questions(meeting_id)
    for question in questions:
        if question.get("status") == "No":
            current_question = question
            questions.remove(question)
            break
    current_meeting = DB.get_meeting(meeting_id)
    title = current_meeting.get('title')
    return render_template("html/home.html", questions=questions, current_question= current_question, meeting_title=title)

if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    login_manager = LoginManager(app)
    app.run(port=5000, debug=True)