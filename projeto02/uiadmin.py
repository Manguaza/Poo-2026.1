from views import View

class UIAdmin: # classe estática -> não tem instância
    def menu():
        print("Clientes   : 1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print("Categorias : 5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print("9-Sair")
        op = int(input("Informe uma opção: "))    
        try:       
            if op == 1: UIAdmin.cliente_inserir()
            if op == 2: UIAdmin.cliente_listar()
            if op == 3: UIAdmin.cliente_atualizar()
            if op == 4: UIAdmin.cliente_excluir()
            if op == 5: UIAdmin.categoria_inserir()
            if op == 6: UIAdmin.categoria_listar()
            if op == 7: UIAdmin.categoria_atualizar()
            if op == 8: UIAdmin.categoria_excluir()
            if op == 9: return 9
        except ValueError as erro:
            print(" ---- Erro ---->", erro)

    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        senha = input("Informe a senha: ")
        View.cliente_inserir(nome, email, fone, senha)

    def cliente_listar():
        for obj in View.cliente_listar(): print(obj)       

    def cliente_atualizar():
        UIAdmin.cliente_listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        senha = input("Informe a nova senha: ")
        View.cliente_atualizar(id, nome, email, fone, senha)

    def cliente_excluir():
        UIAdmin.cliente_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.cliente_excluir(id)

    def categoria_inserir():
        descricao = input("Informe a descrição: ")
        View.categoria_inserir(descricao)

    def categoria_listar():
        for obj in View.categoria_listar(): print(obj)      

    def categoria_atualizar():
        UIAdmin.categoria_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        View.categoria_atualizar(id, descricao)

    def categoria_excluir():
        UIAdmin.categoria_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.categoria_excluir(id)

