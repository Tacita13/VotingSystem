from flask import Flask
from flask_login import LoginManager
from mockdbhelper import MockDBHelper as DBHelper
from user import User
from index import index
from login import login, logout, register_page, register
from home import home
from meeting import meeting
#from voting import voting
#from results import results

app = Flask(__name__)
login_manager = LoginManager(app)
app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
DB = DBHelper()

app.add_url_rule("/", "index", index, methods=['GET', 'POST'])
app.add_url_rule("/login", "login", login, methods=['GET', 'POST'])
app.add_url_rule("/logout", "logout", logout, methods=['GET', 'POST'])
app.add_url_rule("/register_page", "register_page", register_page, methods=['GET', 'POST'])
app.add_url_rule("/register", "register", register, methods=['GET', 'POST'])
app.add_url_rule("/home", "home", home, methods=['GET', 'POST'])
app.add_url_rule("/meeting", "meeting", meeting, methods=['GET', 'POST'])
#app.add_url_rule("/voting", "voting", voting, methods=['GET', 'POST'])
#app.add_url_rule("/results", "results", results, methods=['GET', 'POST'])

@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)

if __name__ == "__main__":
    app.run()