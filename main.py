import os
import smtplib
from flask import Flask, render_template, url_for, redirect, flash, request
from forms import LoginForm
from forms import RegisterForm
# from flask_sqlalchemy import SQLAlchemy

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


posts = [
    {
        'author': "Sevil Rasulova",
        'title': "Post 1",
        'content': "Post 1 Content",
        'date': "26-Sep"
    },
    {
        'author': "Anar Rzayev",
        'title': "Post 2",
        'content': "Post 2 Content",
        'date': "27-Sep"
    },
    {
        'author': "Zəhra Bayramlı",
        'title': "Post 3",
        'content': "Post 3 Content",
        'date': "28-Sep"
    }
]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardsecretkey'
# app.config['SQLALCHEMY DATABASE URI'] = 'mysql://root:''@localhost/flaskdb'
# app.config['SQLALCHEMY TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
# class UserInfo(db.Model):
#     id = db.Column (db.Integer, primary_key = True)
#     email = db.Column (db.String(100), unique = True)
#     password = db.Column(db.String(100))
#
#     def __init__(self, email, password):
#         self.email = email
#         self.password = password

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/haqqımızda")
def about():
    return render_template('about.html', title='Haqqımızda')

@app.route("/daxil-ol", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if request.form['email'] != 'sevillerasulova@gmail.com' or request.form['password'] != '123':
            flash("Yanlış Məlumat Daxil Etmisiniz, Yenidən Cəhd Edin")
        else:
            return redirect(url_for('home'))

    return render_template('login.html', title='Daxil Ol', form=form)

# @app.route("/register")
# def reg():
#     form = RegisterForm()
#     return render_template('register.html', title='Qeydiyyat')

@app.route("/qeydiyyat", methods=['GET', 'POST'])
def register():
    # name = request.form.get("name")
    # email = request.form.get("email")
    # password = request.form.get("password")
    form = RegisterForm()
    if form.validate_on_submit():
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            subject = "From Mathology"
            body = "You are registered"
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail(EMAIL_ADDRESS, request.form['email'], msg)
        return render_template('reg_success.html', title='Qeydiyyat')

    return render_template('register.html', title='Qeydiyyat', form=form)

    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # server.ehlo()
    # server.starttls()
    # server.login(config.EMAIL_ADDRESS, config.PASSWORD)
    # server.sendmail(config.EMAIL_ADDRESS, request.form['email'], message)

@app.route('/riyaziyyat-olimpiadaları')
def olympiad():
    return render_template('olympiad.html', title="Riyaziyyat Olimpiadaları")

@app.route('/məsləhət-bloqu')
def advice():
    return render_template('blog.html', title="Məsləhət Bloqu", posts=posts)

@app.route('/müzakirə')
def discuss():
    return render_template('discuss.html', title="Müzakirə")



if __name__ == '__main__':
    app.run(debug=True)