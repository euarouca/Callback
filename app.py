from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_url = "https://api.digikey.com/v1/oauth2/token"
    data = {
        "client_id": "SEU_CLIENT_ID",
        "client_secret": "SEU_CLIENT_SECRET",
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": "https://api.lucasdanconia.com/callback"
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get('access_token')
    # Salve o token ou use-o imediatamente
    return "Autenticação concluída! Token: " + access_token