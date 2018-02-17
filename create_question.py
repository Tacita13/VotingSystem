from flask import Flask, render_template, request, redirect
from flask_login import login_required, LoginManager,current_user
from dbhandler import get_Question, set_question, get_question_idx
from random import randint
from datetime import datetime

@login_required
def create_question():
    group_name="prueba01"
    if  request.method == 'POST':
        question_creator = request.form.get("formulator")
        if question_creator == "":
            return render_template("html/create_question.html", text1="llenalo")
        question_type = request.form.get("question_type")
        if question_type == "":
            return render_template("html/create_question.html", text2="llenalo")
        question = request.form.get("question")
        if question == "":
            return render_template("html/create_question.html", text3="llenalo")
        question_description = request.form.get("question_description")
        if question_description == "":
            return render_template("html/create_question.html", text4="llenalo")
        question_author = request.form.get("question_author")
        if question_author == "":
            return render_template("html/create_question.html", text5="llenalo")
        id = get_question_idx()

        newId = randint(1, 100)
        while newId in id:
            newId = randint(1, 100)
        set_it = newId
        current_question = {'question_id': set_it, 'user_id': current_user.email, 'group_name': group_name,
                            'question_creator': question_creator, 'question_type': question_type,
                            'question_title': question,
                            'question_description': question_description, 'voting_status': "In-progress",
                            'question_author': question_author, "date_created": "--la fecha va aqui--"}

        # set_question(current_question
    else:
        print ("No")

    return render_template("html/create_question.html")


