from flask import Flask, render_template, request
from flask_login import login_required, LoginManager, current_user
from dbhandler import  get_user_type, get_Result
import ast

@login_required
def results():
    type = get_user_type(current_user.email)
    user_type = type["user_type"]
    group_name = "prueba01"
    question_id = request.form.get("question")
    question_dict = get_Result(question_id)
    print question_dict
    return render_template("html/results.html", question=question_dict['question_title'], question_dict=question_dict, user_type=user_type)