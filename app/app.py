from flask import Flask             #facilitate flask webserving
from flask import render_template, request   #facilitate jinja templating
from flask import session, redirect, url_for, make_response        #facilitate form submission
import os 
from test_stuff import *

#the conventional way:
#from flask import Flask, render_template, request

#redirect url to the specific links from the html templates

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)
@app.route('/')
def index():
    return redirect("/home")

@app.route('/home')
def home():
    return render_template("home_page.html")

@app.route("/target_info",  methods=['GET', 'POST'])
def target_info():
    
    targetName = request.form.get('targetName')
    targetSurname = request.form.get('targetSurname')
    targetNickname = request.form.get('targetNickname')
    targetBirthday= request.form.get('targetBirthday')
    partnerName= request.form.get('partnerName')
    partnerNickname= request.form.get('partnerNickname')
    partnerBirthday = request.form.get('partnerBirthday')
    childName = request.form.get('childName')
    childNickname= request.form.get('childNickname')
    childBirthday= request.form.get('childBirthday')
    petName= request.form.get('petName')
    company= request.form.get('company')
    keywords = request.form.get('keywords')
    #specialChars = request.form.get('specialChars')
    #randomNumbers = request.form.get('randomNumbers')
    #leet = request.form.get('leet')
    read_config("cupp.cfg")
    x = noninteractive(targetName, targetSurname, targetNickname, targetBirthday, partnerName, partnerNickname, partnerBirthday, childName, childNickname, childBirthday, petName, company,keywords, specialChars, randomNumbers, leet)
    print(x)
    
    """
    profile = {
            "name": "владимир",
            "surname": "путин",
            "nick": "putin",
            "birthdate": "07101952",
            "wife": "людмила",
            "wifen": "ljudmila",
            "wifeb": "06011958",
            "kid": "екатерина",
            "kidn": "katerina",
            "kidb": "31081986",
            "pet": "werny",
            "company": "russian federation",
            "words": ["Крим"],
            "spechars1": "y",
            "randnum": "y",
            "leetmode": "y",
            "spechars": [],
        }
    read_config("cupp.cfg")
    x = generate_wordlist_from_profile(profile)
    """
    return render_template("response.html",a=x)

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
    #db.commit()
    #db.close()
