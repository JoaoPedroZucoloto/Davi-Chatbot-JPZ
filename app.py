import os, sys
from flask import Flask,request
app = Flask(__name__)

VERIFY_TOKEN = "chupacabra"

@app.route('/webhook', methods=['GET'])
def index():
    return "This is a Facebook Messenger test bot server."


@app.route('/webhook', methods=['GET'])
def verify():
    # webhook verification
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return 'Verification token missmatch', 403