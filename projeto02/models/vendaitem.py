import json
from DAO import DAO
class VendaItem:
    def __init__(self, id, quantidade, preco, idvenda, idproduto):
        self.id = id
        self.quantidade = quantidade
        self.preco = preco
        self.idvenda = idvenda
        self.idproduto = idproduto
        
class VendaItemDAO(DAO):
    arquivo = "venda_itens.json"
    classe_modelo = VendaItem
    objetos = []