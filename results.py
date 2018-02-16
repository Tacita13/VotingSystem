from flask import Flask, render_template, request
from flask_login import login_required, LoginManager
from dbhandler import get_Question
import ast

@login_required
def results():
    group_name = "prueba01"
    question_title = request.form.get("question_title")
    question_dict = get_Question(question_title, group_name)
    return render_template("html/results.html", question= question_dict)