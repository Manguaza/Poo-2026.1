from .DAO import DAO


class Venda:
    def __init__(self, id, data, carrinho, total, idcliente, status=None, id_entregador=0, status_entrega="Aguardando alocacao"):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.idcliente = idcliente
        self.status = status if status is not None else ("Finalizada" if self.carrinho else "No carrinho")
        self.id_entregador = id_entregador
        self.status_entrega = status_entrega

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        valor = int(valor)
        if valor < 0:
            raise ValueError("Id da venda nao pode ser negativo")
        self.__id = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valor):
        valor = str(valor).strip()
        if valor == "":
            raise ValueError("Data da venda e obrigatoria")
        self.__data = valor

    @property
    def carrinho(self):
        return self.__carrinho

    @carrinho.setter
    def carrinho(self, valor):
        self.__carrinho = valor if valor is not None else {}

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, valor):
        valor = float(valor)
        if valor < 0:
            raise ValueError("Total da venda nao pode ser negativo")
        self.__total = valor

    @property
    def idcliente(self):
        return self.__idcliente

    @idcliente.setter
    def idcliente(self, valor):
        valor = int(valor)
        if valor < 0:
            raise ValueError("Venda deve possuir cliente")
        self.__idcliente = valor

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        valor = str(valor).strip()
        if valor not in ["No carrinho", "Finalizada", "Cancelada"]:
            raise ValueError("Status da venda invalido")
        self.__status = valor

    @property
    def id_entregador(self):
        return self.__id_entregador

    @id_entregador.setter
    def id_entregador(self, valor):
        valor = int(valor or 0)
        if valor < 0:
            raise ValueError("Id do entregador nao pode ser negativo")
        self.__id_entregador = valor

    @property
    def status_entrega(self):
        return self.__status_entrega

    @status_entrega.setter
    def status_entrega(self, valor):
        valor = str(valor).strip()
        permitidos = ["Aguardando alocacao", "Preparando", "Saiu para entrega", "Entregue", "Cancelada"]
        if valor not in permitidos:
            raise ValueError("Status de entrega invalido")
        self.__status_entrega = valor

    def __str__(self):
        return f"Venda {self.id} - {self.data} - {self.total} - {self.status}"

    def to_json(self):
        return {
            "id": self.id,
            "data": self.data,
            "carrinho": self.carrinho,
            "total": self.total,
            "idcliente": self.idcliente,
            "status": self.status,
            "id_entregador": self.id_entregador,
            "status_entrega": self.status_entrega
        }


class VendasDAO(DAO):
    arquivo = "vendas.json"
    classe_modelo = Venda
    objetos = []
