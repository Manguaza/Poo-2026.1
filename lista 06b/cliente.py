import json

class Cliente:
    def __init__(self, id, nome): #, email, fone):
        self.id = id
        self.nome = nome
        #self.email = email
        #self.fone = fone
    def __str__(self):
        return f"{self.id} - {self.nome}" # - {self.email} - {self.fone}"
    
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

