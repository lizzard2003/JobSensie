# this app is made to as user questions about themselves to choose a careerpath
# we are using flask
from flask import Flask, render_template, request, redirect, session
import requests

app = Flask(__name__)



@app.route("/")
def index():
    # Check if the user is logged in
    if "username" in session:
        # Render the mood page
        return redirect("/mood")
    else:
        # Render the login page
        return render_template("login.html")


# Define the login page route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        username = request.form["username"]
        password = request.form["password"]
        
        if username == "myusername" and password == "mypassword":
        
            session["username"] = username
            # bk home page
            return redirect("/")
        else:
        
            return render_template("login.html", error="Invalid username or password")
    else:
        # Render the login page
        return render_template("login.html")
    
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        
        username = request.form["username"]
        password = request.form["password"]
       
        return redirect("/login")
    else:
        # Render
        return render_template("signup.html")