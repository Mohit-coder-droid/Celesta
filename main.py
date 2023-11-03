from flask import Flask,render_template,request,url_for,redirect, url_for, session, g
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import os

# Connecting to the database
db_config = {
    "host":"localhost",
    "database":"celesta",
    "user":"root",
    "password":""
}

# Making parameters configurable
params={
    "local_server":"True",
    "local_uri":"mysql://root:@localhost/celesta",
    "prod_uri":"mysql://root:@localhost/celesta"
}

# Connecting with database and bringing back the data
def data_conn(query):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data

def login_auth(mob_no,pwd):
    # Connecting with database
    '''For making login possible'''

    # Now I need to check whether this user exists or not, and if it exists , then give it's data
    try:
        query = f"SELECT * from contact where mobile_nu='{mob_no}'"
        data = data_conn(query)

        if (data[0][5]==pwd):
            login_data = {
                'result':'True',
                'data': data[0]
            }

        else:
            login_data={
                'result':'False'
            }

    # if the user doesn't exist
    except:
        login_data = {
            'result':'False'
        }

    return login_data


app = Flask(__name__)
app.secret_key = os.urandom(24)

local_server = True

# If we are working on our local server then we will use our local database
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]

db = SQLAlchemy(app)

# Contact us databasae table
class Contact(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    firstName = db.Column(db.String(50),nullable=False)
    lastName = db.Column(db.String(50))
    mobile_nu = db.Column(db.Integer,nullable=False)
    email = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)

class Medicine(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    medicine = db.Column(db.String(100),nullable=False)
    usrno = db.Column(db.Integer,nullable=False)
    time = db.Column(db.String(20),nullable=False)

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

@app.route("/login",methods=["POST","GET"])
def login():

    if (request.method=="POST"):
        mob_no = request.form['mob_no']
        pwd = request.form['pwd']

        login_data = login_auth(mob_no,pwd)

        
        # If we agreed it's login then store it's data
        if login_data['result']=='True':
            session['user_data'] = g.user_data =  login_data['data']
            session['user'] = g.user = login_data['data'][1]

            # Loading medicines
            query = f"SELECT * from medicine WHERE  usrno='{g.user_data[0]}'"
            data = data_conn(query)
            session['usr_med'] = g.usr_med = data

        return login_data
    
    return render_template('login.html')

@app.route('/medicine', methods=['GET','POST'])
def medicine():
    if (request.method=='POST'):
        medicine_ = request.form['medicine']
        time_ = request.form['time']
        usrno_ = request.form['usrno']

        entry = Medicine(medicine=medicine_,time=time_,usrno=usrno_)

        db.session.add(entry)
        db.session.commit()

        return 'Successful'

@app.before_request
def before_request():
    g.user = 'None'
    g.user_data = 'None'
    g.usr_med = 'None'
    g.no_med = 'None'

    if 'user' in session:
        g.user = session['user']
        g.user_data = session['user_data']
        g.usr_med = session['usr_med']
        g.no_med = len(g.usr_med)

# Making logout route
@app.route('/logout')
def logout():
    session.pop('user',None)
    return render_template('{{url_for("/")}}')

@app.route('/article')
def article():
    return render_template('article.html')


app.run(debug=True)
