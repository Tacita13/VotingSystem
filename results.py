from flask import Flask, render_template, request
from flask_login import login_required, LoginManager, current_user
from dbhandler import get_Question, get_user_type
import ast

@login_required
def results():
    type = get_user_type(current_user.email)
    user_type = type["user_type"]
    group_name = "prueba01"
    question = request.form.get("question")
    question_dict = get_Question(question, group_name)
    return render_template("html/results.html", question=question, question_dict=question_dict, user_type=user_type)