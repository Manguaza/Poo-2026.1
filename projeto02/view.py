# View acessa as classes do Modelo
from cliente import Cliente, ClienteDAO
from categoria import Categoria, CategoriaDAO
from produto import Produto, ProdutoDAO
from venda import Venda, VendasDAO
from vendaitem import VendaItem, VendaItemDAO


class View: # nenhum print, nenhum input
    @staticmethod
    def cliente_criar_admin():
        # cria o usuário admin se ele não existir
        for obj in View.cliente_listar():
            if obj.email == "admin": return
        View.cliente_inserir("admin", "admin", "(84)912345678", "1234") 

    @staticmethod
    def cliente_autenticar(email, senha):
        for obj in View.cliente_listar():
            if obj.email == email and obj.senha == senha: 
                return { "id": obj.id, "nome": obj.nome }
        return None

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        ClienteDAO().inserir(c)
        #(new ClienteDAO()).inserir(c) // Java

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "")
        ClienteDAO().excluir(c)

    def categoria_inserir(descricao):
        c = Categoria(0, descricao)
        CategoriaDAO().inserir(c)

    def categoria_listar():
        return CategoriaDAO().listar()

    def categoria_listar_id(id):
        return CategoriaDAO().listar_id(id)

    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO().atualizar(c)

    def categoria_excluir(id):
        c = Categoria(id, "")
        CategoriaDAO().excluir(c)
        
    @staticmethod
    def produto_listar():
        return ProdutoDAO().listar()
    
    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO().listar_id(id)
    
    @staticmethod
    def produto_inserir(descricao, preco, estoque, idcategoria):
        p = Produto(0, descricao, preco, estoque, idcategoria)
        ProdutoDAO().inserir(p)
    
    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, idcategoria):
        p = Produto(id, descricao, preco, estoque, idcategoria)
        ProdutoDAO().atualizar(p)
    
    @staticmethod
    def produto_excluir(id):
        p = Produto(id, "", 0, 0, 0)
        ProdutoDAO().excluir(id)
    
    @staticmethod
    def venda_inserir(data, carrinho, total, idcliente):
        v = Venda(0, data, carrinho, total, idcliente)
        VendasDAO().inserir(v)
        return v.id  # retornar o id da venda criada
    
    @staticmethod
    def venda_listar():
        return VendasDAO().listar()
    
    @staticmethod
    def venda_listar_id(id):
        return VendasDAO().listar_id(id)
    
    @staticmethod
    def venda_listar_por_cliente(idcliente):
        vendas = VendasDAO().listar()
        return [v for v in vendas if v.idcliente == idcliente]
    
    @staticmethod
    def vendaitem_inserir(quantidade, preco, idvenda, idproduto):
        vi = VendaItem(0, quantidade, preco, idvenda, idproduto)
        VendaItemDAO().inserir(vi)    
        
