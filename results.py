from flask import Flask, render_template, request
from flask_login import login_required, LoginManager
from mockdbhelper import MockDBHelper as DBHelper
import ast

@login_required
def results():
    question = request.form.get("question")
    print type(question)

    return render_template("html/results.html", question= question)