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
from flask import Flask, session, url_for
from flask import render_template
from flask import request, redirect
from flask_pymongo import PyMongo
import secrets

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://admin:0UnvepiYIMIZPfib@cluster0.cdko0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

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
    return render_template('index.html')

@app.route('/newreport',methods=['GET', 'POST'])
def newreport():
    return render_template('newreport.html')

# SignUp Route
@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = mongo.db.userinfo
        # search the username in database
        existing_user = users.find_one({'name': request.form['username']})
        existing_email = users.find_one({'email': request.form['email']})

        # if user not in database
        if not existing_user and not existing_email:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            # storing password in plain text is not good.
            # add new user to database
            users.insert_one({'name':username, 'email':email, 'password':password})
            return redirect(url_for('signin'))
        elif existing_user:
            return "Username already registered. Try logging in. If you still want to signup, try with another username."
        elif existing_email:
            return "Email already registered. Try logging in. If you still want to signup, try with another email."
    else:
        return render_template("signup.html")

# SignIn Route
@app.route('/signin',methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]

        lookedup_user = mongo.db.userinfo.find_one({"email":email})

        if lookedup_user:
            if lookedup_user["password"] == password:
                session["name"] = lookedup_user["name"]
                return render_template('index.html')
            else:
                return "Incorrect Password"
        else:
            return "Email doesn't exist. Try again!"
    else:
        return render_template('signin.html')




