#MAPA SOCIAL

##Introdução

O Mapa Social é um exemplo de aplicação web que visa apresentar como construir sitemas de apresentação de dados georreferenciados com base nos moldes dos Geographic Information Sistema (GIS) utilizando tecnologias livres. Nesta aplicação inicial demonstramos como é possível apresentar em um mapa 110 as estações meteorológicas do Estado do Espírito Santo. Para o desenvolvimento da aplicação utilizamos as seguintes tecnologias:

* __Linguagem de Programação__: [Python] (https://www.python.org) 
* __Framework Web__: [Flask](http://flask.pocoo.org)
* __Framework de ORM__: [SQLAlchemy](http://www.sqlalchemy.org) 
* __Banco de dados__: [Postgresql] (http://www.postgresql.org) 
* __Bibliotca de Análise de Dados__: [Pandas](http://pandas.pydata.org)
* __Biblioteca JavaScript para manipulação de mapas__: [LeafLet](http://leafletjs.com)
* __Repositório de códigos__: [Git](https://git-scm.com)

## Alguns problemas ao trabalhar com GIS para internet:

* Dificuldade em converter e analisar dados de diferentes fontes e formatos;
* Dificuldade em plotar pontos em mapas para aplicações que serão utilizadas em diversos dispositivo móveis; 

##Como solucionamos o problemas?

### Converter e analisar dados de diferentes fontes e formatos

Para quem conhece um pouco de programação sabe que essa tarefa é um pouco dificil de ser realizada. Afinal, é necessário pelo menos, saber o formato do arquivo, tratar palavas com acentos e fazer a inserção desses dados na tabela do banco. Dependendo da linguagem e tecnologia a ser utilizada, isso pode gerar alguns dias de trabalho. 

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

Ih agora como lemos esses dados do banco de dados? Bem, para fazer essa tarefa árdua utilizamos o biblioteca __SQLAlchemy__. Através dela é possível 

### Plotar os pontos em mapas para aplicações móveis

Para realizar a plotagem dos pontos em um dispositivo móvel utilizamos a biblioteca JavaScript chamada __Leaflet__. Essa biblioteca foi desenvolvida pela equipe do [Foursquare](https://pt.foursquare.com). Diferente de outras biblioteca de mapas, o Leaflet foi desenvolvida para auxiliar no desenvolvimento de sistemas moveis. Isso pode ser comprovado pelo tamanho dessa, afinal, essa possui apenas 33k de tamanho. Outro ponto importante da biblioteca é simplicidade de uso. Veja o código abaixo:

```javascript
  var map = new L.Map('map');
  var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
  var osm = new L.TileLayer(osmUrl, {minZoom: 3, maxZoom: 12});
  map.setView(new L.LatLng(-20.297618, -40.295777),12);
  map.addLayer(osm);
```
Perceba que o código acima, é possível apresentar um mapa do [OpenStreet Maps](https://www.openstreetmap.org) de uma forma simples. Além disso, o código demonstra como configurar: 
* O máximo e mínimo de zoom que o mapa aceita;
* O ponto central do mapa;

Para plotar um ponto no mapa é um trabalho mais simples do que o ato de criar o mapa. No código abaixo, pedimos ao Leaflet que coloque uma Marker na latitude e longitude desejada e coloque um Popup, acima do ponto, informando o nome da cidade que representa o marker.

```javascript
  L.marker([latitude, longitude]).addTo(map).bindPopup("<br> <b>Cidade: </b>"+value+"</br>");
```

##Instalação

__É importante comentar que a instalação foi realizada em um ambiente Linux__.
Etapas para a construção do ambiente:

* __Instalar Python__: para instalar o python veja o tutorial presente na documentação da linguagem.
* __Instalar o git__: para instalar o git veja o tutorial presente na documentação da ferramenta.
* __Instalar Postgresql__: para instalar o Postgresl veja o tutorial presente na documentação do banco de dados.
* __Instalar Virtualenv__: o Virtualenv é ambiente virtual para desenvolvimento de soluções em python. Através desse é possível isolar o ambiente de desenvolvimento do restante do sistema operacional. Dessa forma, é possível ter diversos ambientes de desenvolvimento com diferentes configurações no mesmo sistema operacional. Para realizar instalação e entender um pouco mais sobre o __Virtualenv__ acesse esse [link](https://pythonhelp.wordpress.com/2012/10/17/virtualenv-ambientes-virtuais-para-desenvolvimento/) 
* __Crie um ambiente virtual de desenvolvimento com Virtualenv__: veja no tutorial como criar um ambiente virtual. Por exemplo: `Virtualenv mapasocial`
* __Ativar o Virtualenv__: ative o virtualenv com o seguinte comando: `source ./mapasocial/bin/activate`
* __Pegar o código do Mapa social no git__: para pegar o código do mapa social basta executar o seguinte comando: `git clone https://github.com/LEDS/MapaSocial.git` 
* __Instalar o Flask, Pandas, SQLAlchemy e tudo mais que precisamos para o projeto e que não foi instalado__: dentro da pasta mapasocial tem um arquivo chamado __requeriment.txt__ que contém o nome de todas as bibliotecas necessárias para que o projeto funcione. Para instalar esses bibliotecas basta executar o seguinte comando: `pip install -r requeriments.txt`. Magicamente o pip irá instalar tudo que é necessário para o projeto.
* __Executar a aplicação__: digite o seguinte comando: `python run.py`. Após isso abra o navegador e digite: `http://localhost:5000` e veja a magia acontecer :)

##Fontes dos dados

O Banco de dados foi gerado a patir de médias mensais referentes ao périodo de 30 anos (1977 a 2006), obtidas por meio do sistema de informações hidrológicas (HidoWEB) da ANA (Agencia Nascional de Águas), INMET (Instituto de Nascional de Meteorologia), INCAPER (Instituto Capixaba de Pesquisa, Assistência Técnica e Extensão Rural). O banco de dados contém somente as seguintes informações:

* Código da estação meteorológicas
* Municipio na qual está a meteorológicas
* Precipitação (Chuva)
* Longitude
* Latitude

##Dicas de leitura
* [__How To Structure Large Flask Applications__](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications)
* [__Integrando SQLAlchemy e Flask__](https://pythonhosted.org/Flask-SQLAlchemy/quickstart.html)
* [__10 minutes to Pandas__](http://pandas.pydata.org/pandas-docs/stable/10min.html)
* [__Virtualenv: Ambientes virtuais para desenvolvimento__](https://pythonhelp.wordpress.com/2012/10/17/virtualenv-ambientes-virtuais-para-desenvolvimento/)


