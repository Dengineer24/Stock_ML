from flask import Flask, render_template, make_response
import json
from random import random 
from time import time 

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    data = [time() * 1000, random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

# Start up 
if __name__ == '__main__':
    app.run()