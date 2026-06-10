from .DAO import DAO


class Entregador:
    def __init__(self, id, nome, email, fone, veiculo):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.veiculo = veiculo

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        valor = int(valor)
        if valor < 0:
            raise ValueError("Id do entregador nao pode ser negativo")
        self.__id = valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        valor = str(valor).strip()
        if valor == "":
            raise ValueError("Nome do entregador e obrigatorio")
        self.__nome = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        valor = str(valor).strip().lower()
        if valor == "" or "@" not in valor:
            raise ValueError("E-mail do entregador invalido")
        self.__email = valor

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, valor):
        self.__fone = str(valor).strip()

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, valor):
        valor = str(valor).strip()
        if valor == "":
            raise ValueError("Veiculo do entregador e obrigatorio")
        self.__veiculo = valor

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.veiculo}"

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "fone": self.fone,
            "veiculo": self.veiculo
        }


class EntregadorDAO(DAO):
    arquivo = "entregadores.json"
    classe_modelo = Entregador
    objetos = []
