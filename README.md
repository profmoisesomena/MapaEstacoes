#MAPA SOCIAL

##Introdução

O Mapa Social é um exemplo de aplicação web que visa apresentar como construir sistemas de apresentação de dados georreferenciados com base nos moldes dos Geographic Information System (GIS) utilizando tecnologias livres.Nesta aplicação inicial demonstramos como é possível apresentar em um mapa 110 estações meteorológicas do estado do Espírito Santo. Para o desenvolvimento da aplicação utilizamos as seguintes tecnologias:

* __Linguagem de Programação__: [Python] (https://www.python.org) 
* __Framework Web__: [Flask](http://flask.pocoo.org)
* __Framework de ORM__: [SQLAlchemy](http://www.sqlalchemy.org) 
* __Banco de dados__: [Postgresql] (http://www.postgresql.org) 
* __Bibliotca de Análise de Dados__: [Pandas](http://pandas.pydata.org)
* __Biblioteca JavaScript para manipulação de mapas__: [LeafLet](http://leafletjs.com)
* __Repositório de códigos__: [Git](https://git-scm.com)

## Alguns problemas encontrados ao trabalhar com GIS para internet:

* Dificuldade em converter e analisar dados de diferentes fontes e formatos;
* Dificuldade em plotar pontos em mapas para aplicações que serão utilizadas em diversos dispositivo móveis; 

##Como solucionamos os problemas?

### Converter e analisar dados de diferentes fontes e formatos

Para quem conhece um pouco de programação sabe que essa tarefa é um pouco difícil de ser realizada. Afinal, é necessário pelo menos, saber o formato do arquivo, tratar palavras com acentos e fazer a inserção desses dados na tabela do banco. Dependendo da linguagem e tecnologia a ser utilizada, isso pode gerar alguns dias de trabalho. 

Para agilizar esse processo utilizamos o __Pandas__. Com poucas linhas conseguimos ler o arquivo com os dados e inseri-los no banco de dados, como pode ser visto no código abaixo:

```python
import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
dados_estacoes =pd.read_csv("estacoes_es.csv", encoding='latin-1',sep=',')
engine = create_engine('postgresql://postgres:123456@localhost:5432/sigmap')
df = pd.DataFrame(dados_estacoes)
df.to_sql('estacoes_es', engine)
```
Perceba no código acima que em poucas linhas conseguimos ler o arquivo csv e salvar no banco de dados de uma forma simples e rápida.

E agora, como lemos esses dados do banco de dados? Bem, para fazer essa tarefa árdua utilizamos o biblioteca __SQLAlchemy__.O SQLAlchemy permite realizar o mapeamento do código do programa como banco de dados de uma forma transparente. A classe Estacao_Meterologica representa as estações meteorologicas e essa está associada a tabela do banco de dados estacao_meteorologica. 

```python
import json
from app import db
from app.gestao_dados.util import Ponto, Base

"""Classe que representando uma Estacao Meterologica """
class Estacao_Meteorologica (Base):

    __tablename__ = 'estacao_meteorologica'

    cod_estacao = db.Column('Estacao',db.String(255), unique=True)
    municipio = db.Column('Municipios',db.String(255))
    chuva =  db.Column('CHUVA',db.Float)
    latitude = db.Column('Y_coord',db.Float)
    longitude = db.Column('X_coord',db.Float)

    def to_JSON(self):
        ponto = Ponto(self.latitude, self.longitude, self.municipio,self.chuva)
        return ponto.to_JSON()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def findAll():
        return Estacao_Meteorologica.query.all()

    @staticmethod
    def find_name(municipio):
        return Estacao_Meteorologica.query.filter_by(municipio = municipio).all()
```
Essa classe permite salvar uma estação meteorológica e buscar todas as estações meteorologicas do Espírito Santo.

Agora como ligar o banco de dados com o mapa? Simples, vamos usar o __Flask__. Através do Flask é possível criar uma aplicação web que pega as informações do banco de dados, através da classe Estacao_Meteorologica, e retorna os dados plotando os pontos na  página web que contém o mapa. 

```python
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
```    
### Plotar os pontos em mapas para aplicações móveis

Para realizar a plotagem dos pontos em um dispositivo móvel utilizamos a biblioteca JavaScript chamada __Leaflet__. Essa biblioteca foi desenvolvida pela equipe do [Foursquare](https://pt.foursquare.com). Diferente de outras bibliotecas de mapas, o Leaflet foi desenvolvida para auxiliar no desenvolvimento de sistemas móveis. Isso pode ser comprovado pelo tamanho dessa, afinal, essa possui apenas 33k de tamanho. Outro ponto importante da biblioteca é simplicidade de uso. Veja o código abaixo:

```javascript
  var map = new L.Map('map');
  var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
  var osm = new L.TileLayer(osmUrl, {minZoom: 3, maxZoom: 12});
  map.setView(new L.LatLng(-20.297618, -40.295777),12);
  map.addLayer(osm);
```
Perceba que com o código acima, é possível apresentar um mapa do [OpenStreet Maps](https://www.openstreetmap.org) de uma forma simples. Além disso, o código demonstra como configurar: 
* O máximo e mínimo de zoom que o mapa aceita;
* O ponto central do mapa;

Para plotar um ponto no mapa é um trabalho mais simples do que o ato de criar o mapa. No código abaixo, pedimos ao Leaflet que coloque uma Marker na latitude e longitude desejada e coloque um Popup, acima do ponto, informando o nome da cidade que representa o marker.

```javascript
   L.marker([latitude, longitude]).addTo(map).bindPopup("<b>Cidade: </b>"+value+" <br> <b>Chuva: </b>"+chuva+" mm");
```

##Instalação

__É importante comentar que a instalação foi realizada em um ambiente Linux__.
Etapas para a construção do ambiente:

* __Instalar Python__: para instalar o python veja o tutorial presente na documentação da linguagem.
* __Instalar o git__: para instalar o git veja o tutorial presente na documentação da ferramenta.
* __Instalar Postgresql__: para instalar o Postgresql veja o tutorial presente na documentação do banco de dados.
* __Instalar Virtualenv__: o Virtualenv é ambiente virtual para desenvolvimento de soluções em python. Através desse é possível isolar o ambiente de desenvolvimento do restante do sistema operacional. Dessa forma, é possível ter diversos ambientes de desenvolvimento com diferentes configurações no mesmo sistema operacional. Para realizar instalação e entender um pouco mais sobre o __Virtualenv__ acesse esse [link](https://pythonhelp.wordpress.com/2012/10/17/virtualenv-ambientes-virtuais-para-desenvolvimento/) 
* __Criar um ambiente virtual de desenvolvimento com Virtualenv__: veja no tutorial como criar um ambiente virtual. Por exemplo: `Virtualenv mapasocial`
* __Ativar o Virtualenv__: ative o virtualenv com o seguinte comando: `source ./mapasocial/bin/activate`
* __Pegar o código do Mapa social no git__: para pegar o código do mapa social basta executar o seguinte comando: `git clone https://github.com/LEDS/MapaSocial.git` 
* __Instalar o Flask, Pandas, SQLAlchemy e tudo mais que precisamos para o projeto e que não foi instalado__: dentro da pasta mapasocial tem um arquivo chamado __requeriment.txt__ que contém o nome de todas as bibliotecas necessárias para que o projeto funcione. Para instalar esses bibliotecas, basta executar o seguinte comando: `pip install -r requeriments.txt`. Magicamente o pip irá instalar tudo que é necessário para o projeto.
* __Executar a aplicação__: digite o seguinte comando: `python run.py`. Após isso abra o navegador e digite: `http://localhost:5000` e veja a magia acontecer :)

##Fontes dos dados

O Banco de dados foi gerado a patir de médias mensais de precipitação referentes ao período de 30 anos (1977 a 2006), obtidas por meio do sistema de informações hidrológicas (HidoWEB) da ANA (Agencia Nascional de Águas), INMET (Instituto de Nascional de Meteorologia), INCAPER (Instituto Capixaba de Pesquisa, Assistência Técnica e Extensão Rural). Para nosso exemplo, o banco de dados contém somente as seguintes informações:
* Código das estações meteorológicas
* Municipio na qual estão as estações meteorológicas
* Precipitação (Chuva)
* Longitude
* Latitude

##Dicas de leitura
* [__How To Structure Large Flask Applications__](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications)
* [__Integrando SQLAlchemy e Flask__](https://pythonhosted.org/Flask-SQLAlchemy/quickstart.html)
* [__10 minutes to Pandas__](http://pandas.pydata.org/pandas-docs/stable/10min.html)
* [__Virtualenv: Ambientes virtuais para desenvolvimento__](https://pythonhelp.wordpress.com/2012/10/17/virtualenv-ambientes-virtuais-para-desenvolvimento/)
* [__Construindo uma aplicação com Flask, Postgresql e OpenShift__](https://blog.openshift.com/build-your-app-on-openshift-using-flask-sqlalchemy-and-postgresql-92/)
* [__Obtendo imagens de satelites__](http://www.dgi.inpe.br/CDSR/)
* [__15 Free Satellite Imagery Data Sources__](http://gisgeography.com/free-satellite-imagery-data-list/)

##Autores
* [Moises Savedra Omena](prof.moisesomena@gmail.com)
* [Paulo Sérgio dos Santos Júnior](paulossjunior@gmail.com)

