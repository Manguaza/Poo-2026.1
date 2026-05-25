import json
from DAO import DAO

class Venda:
    def __init__(self, id, data, carrinho, total, idcliente, status=None):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.idcliente = idcliente
        self.status = status if status is not None else ("Finalizada" if self.carrinho else "No carrinho")

    def __str__(self):
        return f"Venda {self.id} - {self.data} - {self.total} - {self.status}"

class VendasDAO(DAO):
    arquivo = "vendas.json"
    classe_modelo = Venda
    objetos = []