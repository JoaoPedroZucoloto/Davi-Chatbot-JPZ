import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def nao_entre_em_panico():  
    challenge       = request.args.get('hub.challenge',    default = '*', type = str)
    verify_token    = request.args.get('hub.verify_token', default = '',  type = str)
    print(type(challenge))
    print(type(verify_token))
    if challenge != '*' and verify_token == 'chupacabra':
        return challenge
    else:
        return challenge
       
    data = request.data.decode('utf-8')
    print(data)
        
    return challenge, verify_token

if __name__ == "__main__":
    app.debug = True
    app.run()