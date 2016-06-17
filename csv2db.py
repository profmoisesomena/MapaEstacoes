import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
dados_estacoes =pd.read_csv("estacoes_es.csv", encoding='latin-1',sep=',')
engine = create_engine('postgresql://postgres:123456@localhost:5432/sigmap')
df = pd.DataFrame(dados_estacoes)
df.to_sql('estacao_meteorologica', engine)
