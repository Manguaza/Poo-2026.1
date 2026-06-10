from .DAO import DAO


class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        valor = int(valor)
        if valor < 0:
            raise ValueError("Id da categoria nao pode ser negativo")
        self.__id = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        valor = str(valor).strip()
        if valor == "":
            raise ValueError("Descricao da categoria e obrigatoria")
        self.__descricao = valor

    def __str__(self):
        return f"{self.id} - {self.descricao}"
    
    def to_json(self):
        return {
            "id": self.id,
            "descricao": self.descricao
        }

class CategoriaDAO(DAO):
    arquivo = "categorias.json"
    classe_modelo = Categoria
    objetos = []
