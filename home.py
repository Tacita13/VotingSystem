from flask import Flask, render_template, g
from flask_login import login_required, LoginManager
from mockdbhelper import MockDBHelper as DBHelper
from dbhandler import get_in_progress_question, get_CompletedQuestion


DB = DBHelper()
# User Account
@login_required
def home():
    group_name = "prueba01"
    # print (group_name)
    a = get_in_progress_question(group_name)
    question = get_CompletedQuestion(group_name)
    # print(a)
    autor = a.get("question_author")
    fecha = a.get("date_created")
    tipo = a.get("question_type")
    descripcion = a.get("question_description")
    titulo = a.get("question_title")
    return render_template("html/voting_home.html",question=question, titulo=titulo, descripcion=descripcion,
                           group_name=group_name, autor=autor, fecha=fecha, tipo=tipo)

if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    login_manager = LoginManager(app)
    app.run(port=5000, debug=True)