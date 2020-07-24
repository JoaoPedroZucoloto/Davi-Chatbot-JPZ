import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"
    

if __name__ == "__main__":
    app.run(debug=True)
