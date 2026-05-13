#from cliente import Cliente, ClienteDAO
#from categoria import Categoria, CategoriaDAO
from views import View
from vendaitem import VendaItem, VendaItemDAO

class UI: # classe estática -> não tem instância
    __usuario = None     
    __carrinhos = {}  # id_usuario: {id_produto: quantidade}     

    def menu_visitante():
        print("1-Entrar no Sistema, 2-Abrir Conta, 9-Fim")
        try:
            op = int(input("Informe uma opção: "))           
            if op == 1: UI.visitante_entrar()
            if op == 2: UI.visitante_criar_conta()
            return op
        except ValueError:
            print("Opção inválida. Digite um número.")
            return 0

    def menu_admin():
        print("Clientes   : 1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print("Categorias : 5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print("Produtos   : 10-Inserir, 11-Listar, 12-Atualizar, 13-Excluir")
        print("Vendas     : 14-Listar")
        print("9-Sair")
        try:
            op = int(input("Informe uma opção: "))           
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.categoria_inserir()
            if op == 6: UI.categoria_listar()
            if op == 7: UI.categoria_atualizar()
            if op == 8: UI.categoria_excluir()
            if op == 10: UI.produto_inserir()
            if op == 11: UI.produto_listar()
            if op == 12: UI.produto_atualizar()
            if op == 13: UI.produto_excluir()
            if op == 14: UI.admin_listar_vendas()
            if op == 9: UI.usuario_sair()
            return op
        except ValueError:
            print("Opção inválida. Digite um número.")
            return 0

    def menu_cliente():
        print("1-Listar produtos")
        print("2-Inserir produto no carrinho")
        print("3-Visualizar carrinho")
        print("4-Comprar carrinho")
        print("5-Listar minhas compras")
        print("9-Sair")
        try:
            op = int(input("Informe uma opção: "))           
            if op == 1: UI.produto_listar()
            if op == 2: UI.cliente_inserir_produto_no_carrinho()
            if op == 3: UI.cliente_visualizar_carrinho()
            if op == 4: UI.cliente_comprar_carrinho()
            if op == 5: UI.cliente_listar_compras()
            if op == 9: UI.usuario_sair()
            return op
        except ValueError:
            print("Opção inválida. Digite um número.")
            return 0

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
                    op = UI.menu_admin()
                else:
                    op = UI.menu_cliente()

    @classmethod
    def visitante_entrar(cls):
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        cls.__usuario = View.cliente_autenticar(email, senha)
        if cls.__usuario == None: print("Usuário ou senha inválidos")

    def visitante_criar_conta():
        UI.cliente_inserir()

    @classmethod
    def usuario_sair(cls):
        cls.__usuario = None

    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        senha = input("Informe a senha: ")
        View.cliente_inserir(nome, email, fone, senha)
        #c = Cliente(id, nome, email, fone, senha)
        #View.cliente_inserir(c)

    def cliente_listar():
        for obj in View.cliente_listar(): print(obj)       

    def cliente_atualizar():
        UI.cliente_listar()
        id = (input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        senha = input("Informe a nova senha: ")
        View.cliente_atualizar(id, nome, email, fone, senha)

    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.cliente_excluir(id)

    def categoria_inserir():
        descricao = input("Informe a descrição: ")
        View.categoria_inserir(descricao)

    def categoria_listar():
        for obj in View.categoria_listar(): print(obj)      

    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        View.categoria_atualizar(id, descricao)

    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.categoria_excluir(id)
        
    def produto_listar():
        produtos = View.produto_listar()
        if not produtos:
            print("nenhum produto cadastrado")
        else:
            for p in produtos:
                print(p)
    
    def produto_inserir():
        descricao = input("Informe a descrição: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe o estoque: "))
        UI.categoria_listar()
        idcategoria = int(input("Informe o id da categoria: "))
        View.produto_inserir(descricao, preco, estoque, idcategoria)
    
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe o novo estoque: "))
        UI.categoria_listar()
        idcategoria = int(input("Informe o id da categoria: "))
        View.produto_atualizar(id, descricao, preco, estoque, idcategoria)
    
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.produto_excluir(id)
    
    def cliente_inserir_produto_no_carrinho():
        UI.produto_listar()
        try:
            id_produto = int(input("informe o id do produto: "))
            quantidade = int(input("informe a quantidade: "))
        except ValueError:
            print("Entrada inválida. Digite números.")
            return
        produto = View.produto_listar_id(id_produto)
        if produto is None:
            print("produto não encontrado.")
            return 
        if quantidade <= 0:
            print("quantidade deve ser maior que zero.")
            return
        if quantidade > produto.estoque:
            print("não tem produto suficiente no estoque")
            return
        id_usuario = UI.__usuario["id"]
        if id_usuario not in UI.__carrinhos:
            UI.__carrinhos[id_usuario] = {}
        carrinho = UI.__carrinhos[id_usuario]
        if id_produto in carrinho:
            carrinho[id_produto] += quantidade
        else:
            carrinho[id_produto] = quantidade
        print("produto adicionado ao carrinho.")
        

    def cliente_visualizar_carrinho():
        id_usuario = UI.__usuario["id"]
        carrinho = UI.__carrinhos.get(id_usuario, {})
        if not carrinho:
            print ("carrinho vazio")
            return
        total_carrinho = 0
        print("produtos no carrinho")
        for id_produto, quantidade in carrinho.items():
            produto = View.produto_listar_id(id_produto)
            if produto is None:
                print(f"-produto {id_produto} não encontrado no sistema")
                continue
            total_item = produto.preco * quantidade
            total_carrinho += total_item
            print(f"- {produto.descricao}: R$ {produto.preco:.2f} x {quantidade} = R$ {total_item:.2f}")
        print(f"Total do carrinho: R$ {total_carrinho:.2f}")
        

    def cliente_comprar_carrinho():
        id_usuario = UI.__usuario["id"]
        carrinho = UI.__carrinhos.get(id_usuario, {})
        if not carrinho:
            print("carrinho vazio. Nada para comprar.")
            return
        total = 0
        carrinho_itens = []
        for id_produto, quantidade in carrinho.items():
            produto = View.produto_listar_id(id_produto)
            if produto is None:
                print(f"Produto {id_produto} não encontrado. Compra cancelada.")
                return
            if quantidade > produto.estoque:
                print(f"Estoque insuficiente para {produto.descricao}. Compra cancelada.")
                return
            preco_item = produto.preco * quantidade
            total += preco_item
            carrinho_itens.append((id_produto, quantidade, produto.preco))
        # Criar venda
        data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        id_venda = View.venda_inserir(data, carrinho, total, id_usuario)
        # Criar itens da venda
        for id_produto, quantidade, preco in carrinho_itens:
            View.vendaitem_inserir(quantidade, preco, id_venda, id_produto)
            # Deduzir estoque
            produto = View.produto_listar_id(id_produto)
            View.produto_atualizar(id_produto, produto.descricao, produto.preco, produto.estoque - quantidade, produto.idcategoria)
        # Limpar carrinho
        UI.__carrinhos[id_usuario] = {}
        print(f"Compra realizada com sucesso! Total: R$ {total:.2f}")

    def cliente_listar_compras():
        id_usuario = UI.__usuario["id"]
        vendas = View.venda_listar_por_cliente(id_usuario)
        if not vendas:
            print("Nenhuma compra encontrada.")
            return
        for venda in vendas:
            print(f"Venda ID: {venda.id} - Data: {venda.data} - Total: R$ {venda.total:.2f} - Status: {venda.status}")
            # Listar itens
            itens = [vi for vi in VendaItemDAO().listar() if vi.idvenda == venda.id]
            for item in itens:
                produto = View.produto_listar_id(item.idproduto)
                if produto:
                    print(f"  - {produto.descricao}: {item.quantidade} x R$ {item.preco:.2f} = R$ {item.quantidade * item.preco:.2f}")
                else:
                    print(f"  - Produto ID {item.idproduto}: {item.quantidade} x R$ {item.preco:.2f}")

    def admin_listar_vendas():
        vendas = View.venda_listar()
        if not vendas:
            print("Nenhuma venda encontrada.")
            return
        for venda in vendas:
            cliente = View.cliente_listar_id(venda.idcliente)
            nome_cliente = cliente.nome if cliente else f"Cliente ID {venda.idcliente}"
            print(f"Venda ID: {venda.id} - Cliente: {nome_cliente} - Data: {venda.data} - Total: R$ {venda.total:.2f} - Status: {venda.status}")
            # Listar itens
            itens = [vi for vi in VendaItemDAO().listar() if vi.idvenda == venda.id]
            for item in itens:
                produto = View.produto_listar_id(item.idproduto)
                if produto:
                    print(f"  - {produto.descricao}: {item.quantidade} x R$ {item.preco:.2f} = R$ {item.quantidade * item.preco:.2f}")
                else:
                    print(f"  - Produto ID {item.idproduto}: {item.quantidade} x R$ {item.preco:.2f}")

UI.main()
