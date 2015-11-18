import json
from app import db
import socket, struct, fcntl
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

class endereco():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockfd = sock.fileno()
    SIOCGIFADDR = 0x8915

    def get_ip(iface = 'eth0'):
        ifreq = struct.pack('16sH14s', iface, socket.AF_INET, '\x00'*14)
        try:
            res = fcntl.ioctl(sockfd, SIOCGIFADDR, ifreq)
        except:
            return None
        ip = struct.unpack('16sH2x4s8x', res)[2]
        return socket.inet_ntoa(ip)
