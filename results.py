from flask import Flask, render_template, request
from flask_login import login_required, LoginManager
from dbhandler import get_Question
import ast

@login_required
def results():
    group_name = "prueba01"
    question = request.form.get("question")
    question_dict = get_Question(question, group_name)
    return render_template("html/results.html", question=question, question_dict=question_dict)