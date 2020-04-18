# Application 9: Database that stores
# the email addresses and heights of its users.
# When a user enters their email and height,
# an email will be sent with their height and the
# average height of all users in the database.import os, sys 



from flask import Flask, render_template, request
# Gets the SQLAlchmey library from flask      
from flask_sqlalchemy import SQLAlchemy
# Gets the average function
from sqlalchemy import func
# Gets send_email function
from send_email import send_email

app=Flask(__name__)
# Connects to database on Heroku servers
app.config['SQLALCHEMY_DATABASE_URI']='postgres://vyoomnbjlrnivp:05a067687a795189615e3e00ac24602ba69f87672a768f0a3dfe727c67f34979@ec2-34-202-7-83.compute-1.amazonaws.com:5432/da7stu0j3fre9d?sslmode=require'
# Creates database
db = SQLAlchemy(app)

class Data(db.Model):
    # Name of table
    __tablename__="data"
    # ID column that gives unique number to each data set
    id = db.Column(db.Integer,primary_key=True)
    # Email column with maximum limit of 120 and they must be unique
    email_ = db.Column(db.String(120), unique=True)
    # Height column that accepts integers
    height_ = db.Column(db.Integer)
    
    # Initialises all the variables
    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

@app.route("/")

def index():
    # Renders the index.html homepage on first page
    return render_template("index.html")

# POST is required as FORM is set to POST method
@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        # Gets email and height from server
        email = request.form["email_name"]
        height = request.form["height_name"]
        # Outputs email and height to terminal
        print(email, height)
        # If email is unique (not in database) add data to database
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            # Sends email and height to init method in class Data
            data = Data(email, height)
            # Creates email and height column
            db.session.add(data)
            db.session.commit()
            # Gets the average height as a number using the avg function
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            # Rounds average to 1 decimal place 
            average_height = round(average_height,1)
            count = db.session.query(Data.height_).count()
            # Calls send_email function
            send_email(email, height, average_height, count)
            # Returns success webpage
            return render_template("success.html")
        # If email is in database, refresh page to index.html
        else:
            # Message appears above email field
            return render_template("index.html", 
            text="It seems we've got this email already. Please give us a new email.")


if __name__ == '__main__':
    app.debug=True
    # Sets name of IP to 5001 and runs
    # the app
    app.run(port=5001)