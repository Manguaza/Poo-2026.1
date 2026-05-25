from views import View

class UICliente: # classe estática -> não tem instância
    def menu():
        print("1-Listar produtos")
        print("2-Inserir produto no carrinho")
        print("3-Visualizar carrinho")
        print("4-Comprar carrinho")
        print("5-Listar minhas compras")
        print("9-Sair")
        op = int(input("Informe uma opção: "))           
        if op == 1: pass
        if op == 2: pass
        if op == 3: pass
        if op == 4: pass
        if op == 5: pass
        if op == 9: return 9
