from flask import Flask, render_template, g, request, redirect
from flask_login import login_required, LoginManager, current_user
from mockdbhelper import MockDBHelper as DBHelper
from dbhandler import get_in_progress_question, get_CompletedQuestion, get_user_type
from user import User

# User Account
@login_required
def home():
    type = get_user_type(current_user.email)
    if type["user_type"] == "Student":
        pass
    else:
        return redirect('/home')
    group_name = "prueba01"
    # print (group_name)
    a = get_in_progress_question(group_name)
    questions = get_CompletedQuestion(group_name)


    autor = a.get("question_author")
    fecha = a.get("date_created")
    tipo = a.get("question_type")
    descripcion = a.get("question_description")
    titulo = a.get("question_title")

    voto = request.form.get("myText")
    if None != voto:
        print (voto)
    else:
        print "No voto"

    return render_template("html/voting_home.html", questions=questions, titulo=titulo, descripcion=descripcion,current_question = get_in_progress_question(group_name))




if __name__ == "__main__":
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    login_manager = LoginManager(app)
    app.run(port=5000, debug=True)