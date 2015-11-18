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
