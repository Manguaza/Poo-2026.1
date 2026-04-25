import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class categoria:
    def__init__(self, id = int,  descricao = string):
        self.id = id
        self.descricao =  string
        det__str__(self):
            return "{self.id} - {self.descricao}"
        
        
class venda: 
  def__init__(self, id = int, data = datatime, carrinho = bool, total = double, idcliente = int):
      self.id = id
      self.data = data
      self.carrinho = carrinho
      self.total = total
      self.idcliente = idcliente
      status = "No carrinho"
      if self__carrinho
      else "finaliza"
      return f"venda {self.id} - {self.data} - {self.total} - {self.status} "
      
class produto: 
    def__init__(self, id = int, descricao = string, preco = double, estoque = int, idcategoria = int)
    self.id = id
    self.decricao = descricao
    self.preco = preco
    self.estoque = estoque
    self.idcategoria = categoria
    
    def__str__(self):
        return f"{self.id} - {self.descricao} - {self.preco} - {self.estoque}"
    
class vendaitem:
    def__init__(self, id = int, quantidade = int, preco = double, idvenda = int, idproduto = int)
    self.id = id
    self.quantidade = quantidade
    self.preco = preco
    self.idvenda = idvenda
    self.idproduto = idproduto
    
  def__str__(self):
       return f"{self.id} - {self.quantidade} - {self.preco} - {self.idvenda} - {self.idproduto}"       
        
class ClienteDAO:
    def __init__(self):
        self.objetos = []
    def inserir(self, obj):
        self.abrir()
        self.objetos.append(obj)
        self.salvar()
    def listar(self):
        self.abrir()
        return self.objetos
    def salvar(self):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)                 
    def abrir(self):
        self.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"])
                    self.objetos.append(c)        
        except FileNotFoundError:
            self.objetos = []
            
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Atualizar 4-Excluir 9-Fim")
        return int(input("Informe uma opção: "))
    @staticmethod
    def inserir():                           # C - Create
        print("Cadastro de Clientes")
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        c = Cliente(id, nome)
        ClienteDAO().inserir(c)
    @staticmethod
    def listar():                            # R - Read
        print("Listagem de Clientes")
        for c in ClienteDAO().listar(): print(c)
    def atualizar():                         # U - Update
        pass
    def excluir():                           # D - Delete
        pass    

UI.main()

