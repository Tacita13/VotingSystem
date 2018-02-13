from flask import Flask, render_template
from flask_login import login_required, LoginManager
from mockdbhelper import MockDBHelper as DBHelper

@login_required
def results():
    pass