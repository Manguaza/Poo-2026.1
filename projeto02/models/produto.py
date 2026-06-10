from .DAO import DAO


class Produto:
    def __init__(self, id, descricao, preco, estoque, idcategoria, imagem=""):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idcategoria = idcategoria
        self.imagem = imagem

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        valor = int(valor)
        if valor < 0:
            raise ValueError("Id do produto nao pode ser negativo")
        self.__id = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        valor = str(valor).strip()
        if valor == "":
            raise ValueError("Descricao do produto e obrigatoria")
        self.__descricao = valor

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        valor = float(valor)
        if valor <= 0:
            raise ValueError("Preco do produto deve ser maior que zero")
        self.__preco = valor

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, valor):
        valor = int(valor)
        if valor < 0:
            raise ValueError("Estoque do produto nao pode ser negativo")
        self.__estoque = valor

    @property
    def idcategoria(self):
        return self.__idcategoria

    @idcategoria.setter
    def idcategoria(self, valor):
        valor = int(valor)
        if valor < 0:
            raise ValueError("Produto deve possuir uma categoria")
        self.__idcategoria = valor

    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, valor):
        self.__imagem = "" if valor is None else str(valor)

    def __str__(self):
        return f"{self.id} - {self.descricao} - {self.preco} - {self.estoque}"

    def to_json(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "preco": self.preco,
            "estoque": self.estoque,
            "idcategoria": self.idcategoria,
            "imagem": self.imagem
        }


class ProdutoDAO(DAO):
    arquivo = "produtos.json"
    classe_modelo = Produto
    objetos = []
