from flask import Flask, request

app = Flask(__name__)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    return f"Código OAuth recebido: {code}", 200
