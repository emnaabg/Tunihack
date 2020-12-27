from flask import Flask, request, Response, jsonify, send_from_directory, abort,render_template,make_response,redirect,url_for,flash
import os
from random import randint
import json
#Login
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length,ValidationError
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text


# Initialize Flask application
app = Flask(__name__)
#variable globale 
global coord_blocs
coord_blocs=[]
global ww
global hh


# Login
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\MSI\\Documents\\Ossec Hackathon\\Tunihack\\database.db'
# app.config['SQLALCHEMY_DATABASE_URI']="mysql://root@localhost/database"
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db = SQLAlchemy(app)                                     
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50), unique=True,nullable=False)
    password = db.Column(db.String(80))
    last_donation=db.Column(db.DateTime, default=datetime.datetime.utcnow)
    nb_donnation=db.Column(db.Integer,default=0)
    wallet=db.Column(db.Float,default=0)
    Phone=db.Column(db.Integer,default=0)
    def __init__(self, firstname, lastname,email,password):
        self.firstname = firstname
        self.phone = phone
        self.email = email
        self.password = password
class Hospital(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50), unique=True,nullable=False)
    region = db.Column(db.String(50),nullable=False)
    nb_donnations = db.Column(db.Integer,default=0)
    total_donnations=db.Column(db.Float,default=0)
    description=db.Column(db.Text(),nullable=False)

class achievements(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hospital_id = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    Montant=db.Column(db.Float,default=0)
    region=db.Column(db.String(50),nullable=False)
    description=db.Column(db.Text(),nullable=False)
    ddl=db.Column(db.DateTime, nullable=False)
    reason=db.Column(db.Text(),nullable=False)
    expect=db.Column(db.Text(),nullable=False)
    progress_donation=db.Column(db.Float,default=0)




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'),Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    

class RegisterForm_user(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    firstname = StringField('firstname', validators=[InputRequired(), Length(min=5, max=20)])
    phone = StringField('phone', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class RegisterForm_Hospital(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    name = StringField('firstname', validators=[InputRequired(), Length(min=5, max=20)])
    region = StringField('phone', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    description=StringField('phone', validators=[InputRequired(), Length(min=0, max=60)])
class GeneralForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    firstname = StringField('firstname', validators=[InputRequired(),Length(min=4, max=15)])
    lastname = StringField('lastname', validators=[InputRequired(),Length(min=4, max=15)])
    
class SecurityForm(FlaskForm):
    old_password = PasswordField('old_password', validators=[InputRequired(),Length(min=8, max=80)])
    new_password = PasswordField('new_password', validators=[InputRequired(),Length(min=8, max=80)])

@app.route('/')
@app.route('/home')
def home():

    return render_template('index.html')
    
@app.route('/hospitals',methods=['POST','GET'])
def hospitals():      

    return render_template('hospitals.html')

@app.route('/services_details',methods=['POST','GET'])
def services_details():      

    return render_template('services-details.html')

@app.route('/profile',methods=['POST','GET'])
def profile():      

    return render_template('profile.html')

@app.route('/needs',methods=['POST','GET'])
def needs():      

    return render_template('needs.html')

@app.route('/my_account',methods=['POST','GET'])
def my_account():      

    return render_template('my-account.html')

@app.route('/make_donation',methods=['POST','GET'])
def make_donation():      

    return render_template('make_donation.html')

@app.route('/hospital_details',methods=['POST','GET'])
def hospital_details():      

    return render_template('hospital-details.html')

@app.route('/contact',methods=['POST','GET'])
def contact():      

    return render_template('contact.html')

@app.route('/change_password',methods=['POST','GET'])
def change_password():      

    return render_template('change-password.html')

@app.route('/achievements',methods=['POST','GET'])
def achievements():      

    return render_template('achievements.html')

@app.route('/invoices',methods=['POST','GET'])
def invoices():      

    return render_template('invoices.html')
  
#

if __name__ == '__main__':
    app.run(debug=True, host = '127.0.0.1', port=5000)