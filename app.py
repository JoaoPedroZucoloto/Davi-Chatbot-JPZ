from flask import Flask, request, Response

app = Flask(_name_)

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json)
    return Response(status=200)