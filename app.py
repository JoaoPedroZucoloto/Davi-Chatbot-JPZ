from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    print(request.data)
    data = request.get_json()
    return 'ok'
    

if __name__ == "__main__":
    app.run()
