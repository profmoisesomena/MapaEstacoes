from flask import Flask, render_template
from Ponto import Ponto

#Configuration
SECRET_KEY = 'vaimeufilhofunciona'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def index():

    cidades = criandoListaPontos()

    return render_template('index.html',pontos=cidades)

# Lista de cidades a serem plotadas
def criandoListaPontos():
    vitoria = Ponto(-20.297618, -40.295777,"Vitória")
    vilavelha = Ponto(-20.3477821,-40.2949528,"Vila Velha")

    cidades = []
    cidades.append(vitoria)
    cidades.append(vilavelha)

    return cidades

if __name__ == '__main__':
    app.run()
