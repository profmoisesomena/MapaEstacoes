from flask import Flask,jsonify, render_template,Blueprint
from app.gestao_dados.models import Estacao_Meterologica
import json

mod_gestao_dados = Blueprint('gestao_dados', __name__)

@mod_gestao_dados.route('/')
def index():
    return render_template('index.html')

@mod_gestao_dados.route('/pontos')
def estados():

    estacoes_meterologicas = {}

    for estacao_meterologica in Estacao_Meterologica.findAll():
        estacoes_meterologicas[estacao_meterologica.municipio] = estacao_meterologica.to_JSON()

    return json.dumps(estacoes_meterologicas)

def criar_pontos():

    vitoria = Estacao_Meterologica(-20.297618, -40.295777,"Vitoria")
    vilavelha = Estacao_Meterologica(-20.3477821,-40.2949528,"Vila Velha")

    vitoria.save()
    vilavelha.save()
