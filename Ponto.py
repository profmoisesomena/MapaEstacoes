class Ponto:
    """Classe que representa um ponto geografico """
    latitude = None
    longitude = None
    nome_cidade = None
    descricao = None

    def __init__(self, latitude,longitude,nome_cidade):
        self.latitude = latitude
        self.longitude = longitude
        self.nome_cidade = nome_cidade
