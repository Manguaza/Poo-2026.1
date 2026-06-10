from .DAO import DAO


class Promocao:
    def __init__(self, id, idcategoria, inicio, fim, percentual):
        self.id = id
        self.idcategoria = idcategoria
        self.inicio = inicio
        self.fim = fim
        self.percentual = percentual

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        valor = int(valor)
        if valor < 0:
            raise ValueError("Id da promocao nao pode ser negativo")
        self.__id = valor

    @property
    def idcategoria(self):
        return self.__idcategoria

    @idcategoria.setter
    def idcategoria(self, valor):
        valor = int(valor)
        if valor <= 0:
            raise ValueError("Promocao deve possuir categoria")
        self.__idcategoria = valor

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, valor):
        valor = str(valor).strip()
        if valor == "":
            raise ValueError("Data inicial da promocao e obrigatoria")
        self.__inicio = valor

    @property
    def fim(self):
        return self.__fim

    @fim.setter
    def fim(self, valor):
        valor = str(valor).strip()
        if valor == "":
            raise ValueError("Data final da promocao e obrigatoria")
        self.__fim = valor

    @property
    def percentual(self):
        return self.__percentual

    @percentual.setter
    def percentual(self, valor):
        valor = float(valor)
        if valor <= 0 or valor >= 100:
            raise ValueError("Percentual de desconto deve estar entre 0 e 100")
        self.__percentual = valor

    def __str__(self):
        return f"{self.id} - Categoria {self.idcategoria} - {self.percentual}%"

    def to_json(self):
        return {
            "id": self.id,
            "idcategoria": self.idcategoria,
            "inicio": self.inicio,
            "fim": self.fim,
            "percentual": self.percentual
        }


class PromocaoDAO(DAO):
    arquivo = "promocoes.json"
    classe_modelo = Promocao
    objetos = []
