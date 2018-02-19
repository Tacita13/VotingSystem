from flask import  render_template, request
from flask_login import login_required,  current_user
from dbhandler import  get_user_type, get_Result

@login_required
def results():
    type = get_user_type(current_user.email)
    user_type = type["user_type"]
    question_id = request.form.get("question")
    question_dict = get_Result(question_id)
    return render_template("html/results.html", question=question_dict['question_title'], question_dict=question_dict, user_type=user_type)