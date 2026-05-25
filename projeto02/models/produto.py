import json
from DAO import DAO

class Produto:
    def __init__(self, id, descricao, preco, estoque, idcategoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idcategoria = idcategoria

    def __str__(self):
        return f"{self.id} - {self.descricao} - {self.preco} - {self.estoque}"
    
    
class ProdutoDAO (DAO):
    arquivo = "produtos.json"
    classe_modelo = Produto
    objetos = []
