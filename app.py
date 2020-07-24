import os, sys
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify(): 
    return 'ok'

if __name__ == "__main__":
    app.run(debug = True)
