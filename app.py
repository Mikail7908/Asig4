from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and a corresponding request handler function
@app.route('/')
def hello_world():
    return 'My Webpage'