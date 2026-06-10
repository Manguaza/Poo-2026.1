from .DAO import DAO


class VendaItem:
    def __init__(self, id, quantidade, preco, idvenda, idproduto):
        self.id = id
        self.quantidade = quantidade
        self.preco = preco
        self.idvenda = idvenda
        self.idproduto = idproduto

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        valor = int(valor)
        if valor < 0:
            raise ValueError("Id do item da venda nao pode ser negativo")
        self.__id = valor

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor):
        valor = int(valor)
        if valor <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        self.__quantidade = valor

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        valor = float(valor)
        if valor < 0:
            raise ValueError("Preco do item da venda nao pode ser negativo")
        self.__preco = valor

    @property
    def idvenda(self):
        return self.__idvenda

    @idvenda.setter
    def idvenda(self, valor):
        valor = int(valor)
        if valor <= 0:
            raise ValueError("Id da venda do item deve ser maior que zero")
        self.__idvenda = valor

    @property
    def idproduto(self):
        return self.__idproduto

    @idproduto.setter
    def idproduto(self, valor):
        valor = int(valor)
        if valor <= 0:
            raise ValueError("Id do produto do item deve ser maior que zero")
        self.__idproduto = valor

    def __str__(self):
        return f"{self.id} - {self.quantidade} x {self.preco:.2f} - Venda {self.idvenda} - Produto {self.idproduto}"

    def to_json(self):
        return {
            "id": self.id,
            "quantidade": self.quantidade,
            "preco": self.preco,
            "idvenda": self.idvenda,
            "idproduto": self.idproduto
        }


class VendaItemDAO(DAO):
    arquivo = "venda_itens.json"
    classe_modelo = VendaItem
    objetos = []
