from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash

from base import app, db
from base.models import User


#@login_required авторизованный доступ

@app.route('/', methods = ['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login_page():
    login = request.form.get('email')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get('next')

            return redirect(next_page)
        else:
            flash('Логин или пароль некорект')
    else:
        flash('please fill login')
        
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    login = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if  not (login or password or password2):
            flash('Заполните поля')
        elif password != password2:
            flash('Пароли не совпадают')
        else: 
            hash_pwd = generate_password_hash(password)
            new_user = User(login = login, password = hash_pwd)
            db.session.add(new_user)
            db.session.commit()

            return render_template(url_for('login_page'))

    return render_template('register.html')




@app.route('/lougout', methods=['GET', 'POST'])
# @login_required
def lougout():
    lougout_user()
    return redirect(url_for('hello_world'))


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next' + request.url)

    return response