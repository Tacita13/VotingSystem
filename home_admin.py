from flask import Flask, render_template, request,redirect, url_for
from flask_login import login_required, LoginManager,current_user
from dbhandler import get_CompletedQuestion, get_in_progress_question,get_user_type, update_question, get_voteCount, get_QuestionByID, set_result
from random import randint

# User Account
@login_required
def home_admin():
    print("Esto es una prueba")
    type = get_user_type(current_user.email)
    if type["user_type"] == "Staff":
        pass
    else:
        return redirect('/home_admin')
    group_name = "prueba01"
    # print (group_name)
    a = get_in_progress_question(group_name)
    questions = get_CompletedQuestion(group_name)
    print (a[0]['question_id'])


    voto = request.form.get("myText")
    if None != voto:
        print (voto)
    else:
        print "No hay nada"


    return render_template("html/voting_home_admin.html", questions=questions, a=a,
                           current_question=get_in_progress_question(group_name))

def end_vote():
    # Query: Transition question to from In-Progress to Complete.
    group_name = "prueba01"
    question_id = request.form.get('question_id')
    question =  get_QuestionByID(question_id, group_name)
    if update_question(question_id, group_name):
        # Query: Sum up all the results from Voting table and put it in Results table.
        yes = get_voteCount(group_name, question_id, "Yes")['vote_count']
        no = get_voteCount(group_name, question_id, "No")['vote_count']
        abstain = get_voteCount(group_name, question_id, "Abstain")['vote_count']
        print yes
        result = {'result_id': randint(1, 100), 'question_id': question_id, 'question_title': question['question_title'],
                  'question_type': question['question_type'], 'group_name': group_name, 'count_yes': yes,
                  'count_no': no, 'count_abstain': abstain, 'total_voters': int(yes) + int(no) + int(abstain)}
        set_result(result)
    return redirect(url_for('home_admin'))


if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    login_manager = LoginManager(app)
    app.run(port=5000, debug=True)