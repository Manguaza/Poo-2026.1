import json
from DAO import DAO

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.id = id         # atributo de instância
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
    
class ClienteDAO(DAO):
    arquivo = "clientes.json"
    classe_modelo = Cliente
    objetos = []