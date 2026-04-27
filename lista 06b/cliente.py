import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"


class Categoria:
    def __init__(self, id descricao):
        self.id = id
        self.descricao = descricao

    def __str__(self):
        return f"{self.id} - {self.descricao}"


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


class Produto:
    def __init__(self, id, descricao, preco, estoque, idcategoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idcategoria = idcategoria

    def __str__(self):
        return f"{self.id} - {self.descricao} - {self.preco} - {self.estoque}"


class VendaItem:
    def __init__(self, id, quantidade, preco, idvenda, idproduto: int):
        self.id = id
        self.quantidade = quantidade
        self.preco = preco
        self.idvenda = idvenda
        self.idproduto = idproduto

    def __str__(self):
        return f"{self.id} - {self.quantidade} - {self.preco} - {self.idvenda} - {self.idproduto}"


class DAO:
    arquivo = ""
    classe_modelo = None
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        for index, existente in enumerate(cls.objetos):
            if existente.id == obj.id:
                cls.objetos[index] = obj
                cls.salvar()
                return True
        return False

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        original_length = len(cls.objetos)
        cls.objetos = [obj for obj in cls.objetos if obj.id != id]
        if len(cls.objetos) != original_length:
            cls.salvar()
            return True
        return False

    @classmethod
    def salvar(cls):
        with open(cls.arquivo, mode="w") as f:
            json.dump([o.__dict__ for o in cls.objetos], f, indent=2)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open(cls.arquivo, mode="r") as f:
                dicts = json.load(f)
                for d in dicts:
                    obj = cls.classe_modelo(**d)
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass


class ClienteDAO(DAO):
    arquivo = "clientes.json"
    classe_modelo = Cliente
    objetos = []


class ProdutoDAO(DAO):
    arquivo = "produtos.json"
    classe_modelo = Produto
    objetos = []


class CategoriaDAO(DAO):
    arquivo = "categorias.json"
    classe_modelo = Categoria
    objetos = []


class VendasDAO(DAO):
    arquivo = "vendas.json"
    classe_modelo = Venda
    objetos = []


class VendaItemDAO(DAO):
    arquivo = "venda_itens.json"
    classe_modelo = VendaItem
    objetos = []


class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.inserir()
            elif op == 2:
                UI.listar()
            elif op == 3:
                UI.atualizar()
            elif op == 4:
                UI.excluir()

    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Atualizar 4-Excluir 9-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def inserir():
        print("Cadastro de Clientes")
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o telefone: ")
        c = Cliente(id, nome, email, fone)
        ClienteDAO.inserir(c)

    @staticmethod
    def listar():
        print("Listagem de Clientes")
        for c in ClienteDAO.listar():
            print(c)

    @staticmethod
    def atualizar():
        print("Atualizar cliente")
        id = int(input("Informe o id do cliente a atualizar: "))
        cliente = ClienteDAO.listar_id(id)
        if cliente is None:
            print("Cliente não encontrado.")
            return

        nome = input(f"Informe o nome [{cliente.nome}]: ") or cliente.nome
        email = input(f"Informe o email [{cliente.email}]: ") or cliente.email
        fone = input(f"Informe o telefone [{cliente.fone}]: ") or cliente.fone

        cliente.nome = nome
        cliente.email = email
        cliente.fone = fone

        if ClienteDAO.atualizar(cliente):
            print("Cliente atualizado com sucesso.")
        else:
            print("Não foi possível atualizar o cliente.")

    @staticmethod
    def excluir():
        print("Excluir cliente")
        id = int(input("Informe o id do cliente a excluir: "))
        if ClienteDAO.excluir(id):
            print("Cliente excluído com sucesso.")
        else:
            print("Cliente não encontrado.")


if __name__ == "__main__":
    UI.main()
