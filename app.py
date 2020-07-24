import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def nao_entre_em_panico():
    ar = 'Lente Azul'
    challenge       = request.args.get('hub.challenge',    default = '*', type = str)
    verify_token    = request.args.get('hub.verify_token', default = '',  type = str)
    if challenge != '*' and verify_token == 'aqui vai o token que tu configura no Workplace':
        return challenge
    
    data = request.data.decode('utf-8')
    output = request.get_json()
    return output

@app.route("/webhook", methods=['POST'])
def webhook_handle():
    output = request.get_json()
    print(output)
    return 'ok'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
