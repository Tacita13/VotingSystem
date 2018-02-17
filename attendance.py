from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_required, LoginManager, current_user
from dbhandler import  get_deletePermission, get_addPermission, set_groupPermission, delete_Permission
from random import randint


# User Account

@login_required
def attendance():
    group_name = "prueba01"
    users_add = get_addPermission(group_name)
    users_delete = get_deletePermission(group_name)
    return render_template("html/attendance.html", group_name=group_name, users_add=users_add, users_delete= users_delete)

@login_required
def attendance_submit():
    group_name = "prueba01"
    users = request.form.getlist('user')
    for user in users:
        permission = {'permission_id': randint(1, 100), 'group_id': 1, 'username': user,
                      'permission_creator': current_user.email, 'group_name': group_name}
        if not set_groupPermission(permission):
            print permission
    return redirect(url_for('attendance'))

def attendance_delete():
    group_name = "prueba01"
    users = request.form.getlist('user')
    for user in users:
        if not delete_Permission(user, group_name):
            print user
    return redirect(url_for('attendance'))


if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    login_manager = LoginManager(app)
    app.run(port=5000, debug=True)