from flask import Flask, render_template, request, g
from flask_login import login_required, LoginManager
from mockdbhelper import MockDBHelper as DBHelper
from dbhandler import get_in_progress_question

DB = DBHelper()
# User Account
@login_required
def voting():

    group_name = "prueba01"
    # print (group_name)
    a = get_in_progress_question(group_name)
    # print(a)
    autor = a.get("question_author")
    fecha = a.get("date_created")
    tipo = a.get("question_type")





    return render_template("html/voting_prompt.html",autor=autor, fecha=fecha, tipo=tipo)

if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    login_manager = LoginManager(app)
    app.run(port=5000, debug=True)