from flask import Flask, render_template, request, redirect
from flask_login import login_required, LoginManager,current_user
from dbhandler import get_Question, set_question, get_question_idx, get_user_type, get_in_progress_question, get_CompletedQuestion
from random import randint
from datetime import datetime

@login_required
def create_question():
    type = get_user_type(current_user.email)
    if type["user_type"] == "Staff":
        pass
    else:
        return redirect('/home_admin')
    group_name="prueba01"
    valid1= False
    valid2= False
    valid3= False
    valid4= False
    valid5 = False
    if  request.method == 'POST':
        question_creator = request.form.get("formulator")
        if question_creator == "":
            text1 = "FILL"
        else:
            text1 = ""
            valid1 = True
        question_type = request.form.get("question_type")
        if question_type == "":
            text2 = "FILL"
        else:
            text2 = ""
            valid2 = True
        question = request.form.get("question")
        if question == "":
            text3 = "FILL"
        else:
            text3 = ""
            valid3 = True
        question_description = request.form.get("question_description")
        if question_description == "":
            text4 = "FILL"
        else:
            text4 = ""
            valid4 = True

        question_author = request.form.get("question_author")
        if question_author == "":
            text5 = "FILL"
        else:
            text5 = ""
            valid5 = True

        if valid1 and valid2 and valid3 and valid4 and valid5:
            id = get_question_idx()

            newId = randint(1, 100)
            while newId in id:
                newId = randint(1, 100)
            set_it = newId
            current_question = {'question_id': set_it, 'user_id': set_it, 'group_name': group_name,
                                'question_creator': question_creator, 'question_type': question_type,
                                'question_title': question,
                                'question_description': question_description, 'voting_status': "In-progress",
                                'question_author': question_author, "date_created": "--la fecha va aqui--"}
            set_question(current_question)
            a = get_in_progress_question(group_name)
            questions = get_CompletedQuestion(group_name)
            return render_template("html/voting_home_admin.html",a=a ,questions=questions)

        return render_template("html/create_question.html", text1=text1, text2=text2, text3=text3, text4=text4, text5=text5)

    return render_template("html/create_question.html")




