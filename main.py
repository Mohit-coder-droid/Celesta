from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/celesta'
db = SQLAlchemy(app)

# Contact us database table
class Sasta_contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200),nullable=False)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contact",methods=["POST","GET"])
def contact():

    if(request.method=="POST"):
        print('request.get_data')
        print(request.form['nm'])   
        name_ = request.form['nm']  #request.args will give us a dictionary with values of input that in the args who had done post rewuest
        email_ = request.form['em'] 
        password_ = request.form['pw']


        # MAking objcet for contact
        entry = Sasta_contact(name=name_,email=email_,password=password_)

        # Now pushing into databasae
        db.session.add(entry)
        db.session.commit()
        return "hi"

    return render_template('sasta_contact.html')

app.run(debug=True)