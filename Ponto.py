from json import JSONEncoder
import json
class Ponto ():
    """Classe que representa um ponto geografico """
    latitude = None
    longitude = None
    nome_cidade = None
    descricao = None

    def __init__(self, latitude,longitude,nome_cidade):
        self.latitude = latitude
        self.longitude = longitude
        self.nome_cidade = nome_cidade

    def __repr__(self):
        return json.dumps(self.__dict__)

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)    
