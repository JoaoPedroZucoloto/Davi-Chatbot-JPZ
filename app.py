import os, sys
from flask import Flask,request
app = Flask(__name__)

VERIFY_TOKEN = "chupacabra"

@app.route('/')
def index():
    return "This is a Facebook Messenger test bot server."

if __name__ == "__main__": 
    app.run() 