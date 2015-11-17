from flask import Flask, render_template,Blueprint
from app.gestao_dados.models import Estacao_Meterologica

mod_gestao_dados = Blueprint('gestao_dados', __name__)

@mod_gestao_dados.route('/')
def index():
    return render_template('index.html')

@mod_gestao_dados.route('/estacoes')
def estacoes():

    estacoes_meterologicas = {}

    for estacao_meterologica in Estacao_Meterologica.findAll():
        estacoes_meterologicas[estacao_meterologica.municipio] = estacao_meterologica.to_JSON()

    return json.dumps(estacoes_meterologicas)
