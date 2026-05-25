from views import View
from uiadmin import UIAdmin
from uicliente import UICliente

class UI: # classe estática -> não tem instância
    __usuario = None     

    def menu_visitante():
        print("1-Entrar no Sistema, 2-Abrir Conta, 9-Fim")
        op = int(input("Informe uma opção: "))           
        if op == 1: UI.visitante_entrar()
        if op == 2: UI.visitante_criar_conta()
        return op

    @classmethod
    def main(cls):
        # verifica a existe o usuário admin
        View.cliente_criar_admin()
        # mostra o menu da aplicação
        UI.menu()
        
    @classmethod
    def menu(cls):
        op = 0
        while op != 9:
            if cls.__usuario == None: 
                # usuário não está logado
                op = UI.menu_visitante()
            else:
                # usuário está logado, verifica se é o admin
                admin = cls.__usuario["nome"] == "admin"
                # mensagem de bem-vindo
                print("IF Comércio Eletrônico 2026.1")
                print("Bem-vindo(a), " + cls.__usuario["nome"])
                # menu do usuário: admin ou cliente
                if admin: 
                    if UIAdmin.menu() == 9: UI.usuario_sair()
                else: 
                    if UICliente.menu() == 9: UI.usuario_sair()

    @classmethod
    def visitante_entrar(cls):
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        cls.__usuario = View.cliente_autenticar(email, senha)
        if cls.__usuario == None: print("Usuário ou senha inválidos")

    def visitante_criar_conta():
        UIAdmin.cliente_inserir()

    @classmethod
    def usuario_sair(cls):
        cls.__usuario = None

UI.main()
