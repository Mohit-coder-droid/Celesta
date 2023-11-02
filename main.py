from flask import Flask,render_template,request,url_for,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json

# Loading config json file
f = open('config.json')
params = json.load(f)["params"]
f.close()

app = Flask(__name__)

local_server = True

# If we are working on our local server then we will use our local database
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]

db = SQLAlchemy(app)

# Contact us database table
class Sasta_contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200),nullable=False)

class Contact(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    firstName = db.Column(db.String(50),nullable=False)
    lastName = db.Column(db.String(50))
    mobile_nu = db.Column(db.Integer,nullable=False)
    email = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contact",methods=["POST","GET"])
def contact():

    if(request.method=="POST"): 
        first_name_ = request.form['first_name']  #request.args will give us a dictionary with values of input that in the args who had done post rewuest
        last_name_ = request.form['last_name'] 
        mob_nu_ = request.form['mob_nu']
        email_ = request.form['email']
        pwd_ = request.form['pwd']


        # MAking objcet for contact
        entry = Contact(firstName=first_name_,lastName=last_name_,mobile_nu=mob_nu_,email=email_,password=pwd_)

        # Now pushing into databasae
        db.session.add(entry)
        db.session.commit()
        return "hi"

    return render_template('signUp.html')

app.run(debug=True)