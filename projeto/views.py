# View acessa as classes do Modelo
from cliente import Cliente, ClienteDAO
from categoria import Categoria, CategoriaDAO

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
        
