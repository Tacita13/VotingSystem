from flask import Flask
from flask_login import LoginManager
from dbhandler import get_user
from user import User
from index import index
from login import login, loginPage, logout
from register import register
from home import home
#from voting import voting
#from results import results

app = Flask(__name__)
login_manager = LoginManager(app)
app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'

#
app.add_url_rule("/", "index", index, methods=['GET', 'POST'])
app.add_url_rule("/loginPage", "loginPage", loginPage, methods=['GET', 'POST'])
app.add_url_rule("/login", "login", login, methods=['GET', 'POST'])
app.add_url_rule("/logout", "logout", logout, methods=['GET', 'POST'])
app.add_url_rule("/home", "home", home, methods=['GET', 'POST'])
#app.add_url_rule("/register_page", "register_page", register_page, methods=['GET', 'POST'])
app.add_url_rule("/register", "register", register, methods=['GET', 'POST'])
#app.add_url_rule("/voting", "voting", voting, methods=['GET', 'POST'])
#app.add_url_rule("/results", "results", results, methods=['GET', 'POST'])

@login_manager.user_loader
def load_user(user_id):
    users = get_user(user_id)
    user = users[0]
    answer = None
    if user['username'].encode('ascii', 'ignore'):
         answer = User(user_id)
    return answer

if __name__ == "__main__":
    app.run()