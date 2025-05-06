from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'App está rodando!'

@app.route('/callback')
def callback():
    code = request.args.get('code')
    return f'Código de autorização recebido: {code}'
