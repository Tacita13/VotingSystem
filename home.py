from flask import Flask, render_template, g, request, redirect
from flask_login import login_required, LoginManager, current_user
from dbhandler import get_in_progress_question, get_CompletedQuestion, get_user_type, set_vote,get_in_progress_question1, get_user_has_vote
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

    voto = request.form.get("myText")
    pregunta = request.form.get("titulo")
    tipo = request.form.get("tipo")
    if None != voto:
        current_question = get_in_progress_question1(group_name,pregunta)

        yavoto = get_user_has_vote(current_user.email,pregunta)
        # print yavoto
        # print "-----------"
        if yavoto == None or (yavoto["voting_id"] ==  None and yavoto['question_title'] == None) :
            vote = {'voting_id':current_user.email, 'question_id':current_question['question_id'], 'group_name':"prueba01",
            'question_title':pregunta, 'question_type':tipo, 'voting_choice':voto}
            set_vote(vote)




    return render_template("html/voting_home.html", questions=questions,a=a ,current_question = get_in_progress_question(group_name))




if __name__ == "__main__":
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    login_manager = LoginManager(app)
    app.run(port=5000, debug=True)