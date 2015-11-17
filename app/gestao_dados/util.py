import json
from app import db
"""Classe para exportar os dados """
class Ponto ():

    nome_cidade = None
    latitude = None
    longitude = None

    def __init__(self, latitude,longitude,municipio,chuva):
        self.latitude = latitude
        self.longitude = longitude
        self.municipio = municipio
        self.chuva = chuva

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

"""Classe base do modelo"""
class Base(db.Model):

    __abstract__  = True

    id            = db.Column('ID',db.Integer, primary_key=True)
    #date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    #date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
    #                                       onupdate=db.func.current_timestamp())
