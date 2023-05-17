from flask import Flask             #facilitate flask webserving
from flask import render_template, request   #facilitate jinja templating
from flask import session, redirect, url_for, make_response        #facilitate form submission
import os 

#the conventional way:
#from flask import Flask, render_template, request

#redirect url to the specific links from the html templates

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)
@app.route('/')
def index():
    if 'username' in session:
        return redirect("/home")
    return render_template('login.html') #edit

@app.route('/login', methods = ['GET','POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if db_tools.verify_account(username,password):
        session['username'] = username
        session['password'] = password
        return redirect("/home")
    if request.form.get('submit_button') is not None:
        return render_template("create_account.html")
    else:
        resp = make_response(render_template('error.html',msg = "username or password is not correct"))
        return resp

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        userIn = request.form.get('username')
        passIn = request.form.get('password') 
        if db_tools.add_account(userIn, passIn) == -1:
            return f"account with username {userIn} already exists"
        else:
            return redirect("/login")
    return redirect(url_for('index'))
    
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect("/login")
    username = session['username']
    password = session['password']
    return render_template("home_page.html", username = username)

def verify_session():
    if 'username' in session and 'password' in session:
        if db_tools.verify_account(session['username'], session['password']):
            return True
    return False

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
    #db.commit()
    #db.close()
