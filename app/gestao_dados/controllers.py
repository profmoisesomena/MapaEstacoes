from flask import Flask, render_template,Blueprint
from app.gestao_dados.models import Estacao_Meteorologica
import json
mod_gestao_dados = Blueprint('gestao_dados', __name__)

@mod_gestao_dados.route('/')
def index():
    return render_template('index.html')

@mod_gestao_dados.route('/estacoes')
def estacoes():

    estacoes_meteorologicas = {}

    for estacao_meteorologica in Estacao_Meteorologica.findAll():
        estacoes_meteorologicas[estacao_meteorologica.municipio] = estacao_meteorologica.to_JSON()


    return json.dumps(estacoes_meteorologicas)

@mod_gestao_dados.route('/municipios/<nome_municipio>')
def municipios(nome_municipio):
    municipios_estacoes={}

    for estacao_meteorologica in Estacao_Meteorologica.find_name(nome_municipio):
        municipios_estacoes[estacao_meteorologica.municipio] =  estacao_meteorologica.to_JSON()

    return json.dumps(municipios_estacoes)
