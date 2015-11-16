from flask import Flask,jsonify, render_template
from Ponto import Ponto
import json
#Configuration
SECRET_KEY = 'vaimeufilhofunciona'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pontos')
def estados():

    #cidades = criandoListaPontos()
    vitoria = Ponto(-20.297618, -40.295777,"Vitoria")
    vilavelha = Ponto(-20.3477821,-40.2949528,"Vila Velha")
    cidades = {}
    cidades["vitoria"] = vitoria.to_JSON()
    cidades["vilavelha"] = vilavelha.to_JSON()
    return json.dumps(cidades)


if __name__ == '__main__':
    app.run()
