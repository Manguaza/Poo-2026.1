import DAO

class Venda:
    def __init__(self, id, data, carrinho, total, idcliente):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.idcliente = idcliente
        self.status = "No carrinho" if self.carrinho else "Finalizada"

    def __str__(self):
        return f"Venda {self.id} - {self.data} - {self.total} - {self.status}"

class VendasDAO:
    arquivo = "vendas.json"
    classe_modelo = Venda
    objetos = []