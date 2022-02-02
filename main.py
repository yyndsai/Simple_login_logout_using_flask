from email.policy import default
from django.shortcuts import render
import flask
from flask import Flask,redirect,session, url_for, request, render_template

app = Flask(__name__)
app.secret_key="Secret Key!"

u_p={'rashi':'rashiPass','yashwanth':'sai'}

@app.route('/user')
def hello_user():
    if 'username' in session:
        return render_template('hello.html',uname=session['username'])
    else:
        return redirect(url_for('index'))

# @app.route('/register')
# def register():
#     return flask.render_template('register.html')
@app.route('/logout')
def logout():
    session.pop('username',None)
    
    return redirect(url_for('index'))

@app.route('/validity', methods=['GET', 'POST'])
def validity():
    if flask.request.method == 'POST':
        username=flask.request.form['name-input']
        password=flask.request.form['name-password']

        if username!='' and password!='' and u_p.get(username,'')==password:
            session['username']=username
            return redirect(url_for('hello_user'))
        else:
            flask.flash("Invalid Credentials")
            return flask.redirect(flask.url_for("index"))

    return flask.render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        username = session['username']
        print(f'session with username{username} is present')
        return redirect(url_for('hello_user'))
    print('session not present')
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

