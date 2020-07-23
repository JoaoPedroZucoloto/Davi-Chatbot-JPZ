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
        return challenge, verify_token
    else:
        return challenge, verify_token
       
    data = request.data.decode('utf-8')
    print(data)
        
    return challenge, verify_token

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)