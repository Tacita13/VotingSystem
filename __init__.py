from flask import Flask
from flask_login import LoginManager
from dbhandler import get_user
from user import User
from index import index
from login import login, loginPage, logout
from register import register
from home import home
from home_admin import home_admin, end_vote
from results import results
from create_question import create_question
from attendance import attendance, attendance_submit, attendance_delete
from vote_page import vote_page


app = Flask(__name__)
login_manager = LoginManager(app)
app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'

#
app.add_url_rule("/", "index", index, methods=['GET', 'POST'])
app.add_url_rule("/loginPage", "loginPage", loginPage, methods=['GET', 'POST'])
app.add_url_rule("/login", "login", login, methods=['GET', 'POST'])
app.add_url_rule("/logout", "logout", logout, methods=['GET', 'POST'])
app.add_url_rule("/home", "home", home, methods=['GET', 'POST'])
app.add_url_rule("/home_admin", "home_admin", home_admin, methods=['GET', 'POST'])
app.add_url_rule("/register", "register", register, methods=['GET', 'POST'])
app.add_url_rule("/results", "results", results, methods=['GET', 'POST'])
app.add_url_rule("/vote_page", "vote-page", vote_page, methods=['GET', 'POST'])
app.add_url_rule("/create_question", "create_question", create_question, methods=['GET', 'POST'])
app.add_url_rule("/attendance", "attendance", attendance, methods=['GET', 'POST'])
app.add_url_rule("/attendance_submit", "attendance_submit", attendance_submit, methods=['GET', 'POST'])
app.add_url_rule("/attendance_delete", "attendance_delete", attendance_delete, methods=['GET', 'POST'])
app.add_url_rule("/end_vote", "end_vote", end_vote, methods=['GET', 'POST'])

@login_manager.user_loader
def load_user(user_id):
    users = get_user(user_id)
    user = users[0]
    answer = None
    if user['username'].encode('ascii', 'ignore'):
         answer = User(user_id)
    return answer

if __name__ == "__main__":
    app.run(port=5000, debug=True)