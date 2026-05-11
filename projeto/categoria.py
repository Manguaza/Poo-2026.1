import json
from DAO import DAO

class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao
    def __str__(self):
        return f"{self.id} - {self.descricao}"
    
class CategoriaDAO:
    arquivo = "categorias.json"
    classe_modelo = Categoria
    objetos = []