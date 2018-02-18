from flask import Flask, render_template, request,redirect
from flask_login import login_required, LoginManager,current_user
from dbhandler import get_CompletedQuestion, get_in_progress_question,get_user_type, update_question


# User Account
@login_required
def home_admin():
    type = get_user_type(current_user.email)
    if type["user_type"] == "Staff":
        pass
    else:
        return redirect('/home_admin')
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

def finish_voting():
    # Query: Transition question to from In-Progress to Complete.
    #group_name = "prueba01"
    #question_title = request.form.get('question_title')
    #if update_question(question_title, group_name):
        # Query: Sum up all the results from Voting table and put it in Results table.
        #SELECT COUNT(voting_choice) FROM Voting  WHERE group_name='Vigilantes'  AND question_title='Destruction of Killgrave'  AND question_type='Proposition' AND voting_choice='Yes'
    #return redirect(url_for('home_admin'))
    pass


if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    login_manager = LoginManager(app)
    app.run(port=5000, debug=True)