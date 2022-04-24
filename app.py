# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from urllib import response
# from TechXUnit4Project.model import check_password_length, check_password_validation, is_empty
from flask import Flask, session, url_for
from flask import render_template
from flask import request, redirect
from flask_pymongo import PyMongo
import secrets
import bcrypt
from model import *
import os

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://admin:0UnvepiYIMIZPfib@cluster0.cdko0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

# For using session object
app.secret_key = secrets.token_urlsafe(16)

#Initialize PyMongo
mongo = PyMongo(app)

# mongo.db.create_collection("test")
# mongo.db.create_collection("userinfo")

# -- Routes section --
# INDEX Route
@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        state_name = request.form["state"]
        return render_template("searchresults.html",state_name=state_name )
       



@app.route('/newreport',methods=['GET', 'POST'])
def newreport():
    if request.method == "POST" and session:
        full_name = request.form['name']
        state = request.form['state']
        description = request.form['description']
        state_crime = mongo.db.StateCrime
        user = mongo.db.report
        user.insert_one({'fullname':full_name,'state':state,"description":description})
        state_crime.insert_one({"state":state,"description":description})
        # calling method from model to get list of US states
        list_state = get_list_states()

        return render_template('newreport.html',list_state=list_state)
    elif session:
        # calling method from model to get list of US states
        list_state = get_list_states()
        
        return render_template('newreport.html',list_state=list_state)
    else:
        return render_template("signin.html")

@app.route('/searchresults', methods = ['GET', 'POST'])
def searchresults():
    descriptions = list(mongo.db.StateCrime.find({}))
    return render_template('searchresults.html')       

# SignUp Route
@app.route('/signup',methods=['GET', 'POST'])
def signup():
    '''
    Functions give two different response on two different requestions. On GET request renders the same page, while on POST
    request perform some operations.
    '''
    # if post request, perform certain operations.
    if request.method == 'POST':
        users = mongo.db.userinfo
        # search the username in database
        name = request.form['username']
        email = request.form['email']
        password_before_encrypting = request.form['password']

        # check if both name and email field are empty.
        if is_empty(name) and is_empty(email):
            return render_template("signup.html", response=True, box=True)
        # check if name field is empty.
        elif is_empty(name):
            return render_template("signup.html", response1=True, box=True)
        # check if the email field is empty.
        elif is_empty(email):
            return render_template("signup.html", response2=True, box=True)
        # check if the length of password is less than 6 or not.
        elif check_password_length(password_before_encrypting):
            return render_template("signup.html", response3=True, box=True)
        # check if the password is validated or not.
        elif check_password_validation(password_before_encrypting):
            return render_template("signup.html", response4=True, box=True)

        existing_user = users.find_one({'name': name})
        existing_email = users.find_one({'email': email})

        # if user not in database
        if not existing_user and not existing_email:
            username = request.form['username']
            email = request.form['email']
            password = password_before_encrypting.encode("utf-8")
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password, salt)

            # add new user to database
            users.insert_one({'name':username, 'email':email, 'password':hashed_password})
            return redirect(url_for('signin'))
        # if user is already registered, renders the same page with a text message.
        elif existing_user:
            return render_template("signup.html", user_in_database=True, box=True)
        # if email is already registered, renders the same page with a text message.
        elif existing_email:
            return render_template("signup.html", email_in_database=True, box=True)
    # if GET request, renders the same page.
    else:
        return render_template("signup.html")

# SignIn Route
@app.route('/signin',methods=['GET', 'POST'])
def signin():
    # if post request, perform certain operations.
    if request.method == 'POST':
        email = request.form["email"]
        password_before_encrypting = request.form["password"]

        # check if the email field is empty.
        if is_empty(email):
            return render_template("signin.html", response2=True, box=True)
        # check if the length of password is less than 6 or not.
        elif check_password_length(password_before_encrypting):
            return render_template("signin.html", response3=True, box=True)
        # check if the password is validated or not.
        elif check_password_validation(password_before_encrypting):
            return render_template("signin.html", response4=True, box=True)

        password = password_before_encrypting.encode("utf-8")

        lookedup_user = mongo.db.userinfo.find_one({"email":email})

        # if email is already registered.
        if lookedup_user:
            # if password is correct.
            if bcrypt.checkpw(password, lookedup_user["password"]):
                session["name"] = lookedup_user["name"]
                return render_template('index.html')
            # if password is incorrect.
            else:
                return render_template('signin.html', password_not_correct=True, box=True)
        # if email is not registered.
        else:
            # if email is not registered, renders the same page.
            return render_template('signin.html', email_not_in_database=True, box=True)
    else:
        # if get request, renders same page.
        return render_template('signin.html')

# Logout Route
@app.route('/logout')
def logout():
    # clear the username from the session data
    session.clear()
    return redirect('/')





