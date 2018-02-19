from flask import Flask, render_template, request
from flask_login import login_required, LoginManager
from dbhandler import get_in_progress_question1

# User Account
@login_required
def vote_page():
    group_name = "prueba01"

    titulo = request.form.get('current_question')
    print titulo
    a = get_in_progress_question1(group_name, titulo )

    descripcion = a.get('question_description')
    autor = a.get('question_author')
    fecha = a.get('question_date')
    tipo = a.get('question_type')

    # esto es solo para testing
    # voto = request.form.get("myText")
    # if None != voto:
    #     print (voto)


    return render_template("html/voting_page.html",titulo=titulo, descripcion=descripcion,
                           group_name=group_name, autor=autor, fecha=fecha, tipo=tipo)

if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'svdVhiUiLWW8X/GRkjxpQbD6F5uxHN4YS307PTeShVJc4E72GfcrtnOeUxlRRKRPSJQDIumkx6B21CUxXTd7LGloQvj0/LSyuub'
    login_manager = LoginManager(app)
    app.run(port=5000, debug=True)