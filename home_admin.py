from flask import Flask, render_template, request
from flask_login import login_required, LoginManager
from dbhandler import get_CompletedQuestion, get_in_progress_question


# User Account
@login_required
def home_admin():
    group_name = "prueba01"
    # print (group_name)
    a = get_in_progress_question(group_name)
    questions = get_CompletedQuestion(group_name)


    descripcion = a.get("question_description")
    titulo = a.get("question_title")

    voto = request.form.get("myText")
    if None != voto:
        print (voto)
    else:
        print "No hay nada"


    return render_template("html/voting_home_admin.html", questions=questions, titulo=titulo, descripcion=descripcion,
                           current_question=get_in_progress_question(group_name))



if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    login_manager = LoginManager(app)
    app.run(port=5000, debug=True)