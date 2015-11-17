import json
from app import db
from app.gestao_dados.util import Ponto

"""Classe base do modelo"""
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())


"""Classe que representando uma Estacao Meterologica """
class Estacao_Meterologica (Base):

    __tablename__ = 'Estacao_Meterologica'

    id = db.Column(db.Integer, primary_key=True)
    nome_cidade = db.Column(db.String(80), unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __init__(self, latitude,longitude,nome_cidade):
        self.latitude = latitude
        self.longitude = longitude
        self.nome_cidade = nome_cidade

    def to_JSON(self):
        ponto = Ponto(self.latitude, self.longitude, self.nome_cidade)
        return ponto.to_JSON()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def findAll():
        return Estacao_Meterologica.query.all()
