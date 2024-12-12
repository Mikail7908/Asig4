from flask import Flask
import sqlite3

def get_db():
    try:
        conn = sqlite3.connect('mydatabase.db')
        return conn
    except sqlite3.Error as e:
        print(e)
        return 

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and a corresponding request handler function
@app.route('/')
def hello_world():
    return 'My Webpage'