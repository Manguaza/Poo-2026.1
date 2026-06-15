from templates.mantercategoria import ManterCategoriaUI
from templates.manterclientes import ManterClienteUI
from templates.manterproduto import ManterProdutoUI
from templates.reajustarproduto import ReajustarProdutoUI
from templates.manterpromocao import ManterPromocaoUI
from templates.manterentregador import ManterEntregadorUI
from templates.manterentrega import ManterEntregaUI
from templates.loginUI import LoginUI
from templates.abrirconta import AbrirContaUI
from view import View
from datetime import datetime, date
from pathlib import Path
import streamlit as st


class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", [
            "Entrar no Sistema",
            "Abrir Conta",
            "Cadastrar Entregador"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
        if op == "Cadastrar Entregador": IndexUI.cadastrar_entregador_visitante()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", [
            "Cadastro de Categorias",
            "Cadastro de Clientes",
            "Cadastro de Produtos",
            "Reajustar Produtos",
            "Controle de Promocoes",
            "Cadastro de Entregadores",
            "Visualizar Vendas",
            "Controle de Entregas"])
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()
        if op == "Reajustar Produtos": ReajustarProdutoUI.main()
        if op == "Controle de Promocoes": ManterPromocaoUI.main()
        if op == "Cadastro de Entregadores": ManterEntregadorUI.main()
        if op == "Visualizar Vendas": IndexUI.visualizar_pedidos_admin()
        if op == "Controle de Entregas": ManterEntregaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", [
            "Listar produtos",
            "Inserir produto no carrinho",
            "Visualizar carrinho",
            "Comprar carrinho",
            "Listar minhas compras"])
        if op == "Listar produtos": IndexUI.listar_produtos_cliente()
        if op == "Inserir produto no carrinho": IndexUI.inserir_produto_no_carrinho()
        if op == "Visualizar carrinho": IndexUI.visualizar_carrinho()
        if op == "Comprar carrinho": IndexUI.comprar_carrinho()
        if op == "Listar minhas compras": IndexUI.listar_compras_cliente()

    def cadastrar_entregador_visitante():
        st.header("Cadastro de Entregador")
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        fone = st.text_input("Fone")
        veiculo = st.text_input("Veiculo")
        if st.button("Cadastrar"):
            try:
                View.entregador_inserir(nome, email, fone, veiculo)
                st.success("Entregador cadastrado com sucesso")
            except Exception as erro:
                st.error(erro)

    def visualizar_pedidos_admin():
        st.header("Vendas")
        vendas = [v for v in View.venda_listar() if v.status == "Finalizada"]
        if len(vendas) == 0:
            st.write("Nenhuma venda cadastrada")
            return

        col1, col2 = st.columns(2)
        with col1:
            inicio = st.date_input("Data inicial", value=date(2000, 1, 1))
        with col2:
            fim = st.date_input("Data final", value=date.today())

        vendas_filtradas = []
        for venda in vendas:
            data_venda = IndexUI.__data_venda(venda)
            if inicio <= data_venda <= fim:
                vendas_filtradas.append(venda)

        if len(vendas_filtradas) == 0:
            st.write("Nenhuma venda encontrada nesse periodo")
            return

        for venda in vendas_filtradas:
            cliente = View.cliente_listar_id(venda.idcliente)
            entregador = View.entregador_listar_id(venda.id_entregador)
            nome_cliente = cliente.nome if cliente else f"Cliente {venda.idcliente}"
            with st.expander(f"Venda {venda.id} - {nome_cliente} - R$ {venda.total:.2f}"):
                st.write(f"Data: {venda.data}")
                st.write(f"Status: {venda.status}")
                st.write(f"Entrega: {venda.status_entrega}")
                st.write(f"Entregador: {entregador.nome if entregador else 'Nao alocado'}")
                itens = IndexUI.__itens_venda(venda.id)
                if len(itens) == 0:
                    st.write("Nenhum item cadastrado para esta venda")
                else:
                    st.dataframe(itens, hide_index=True)

    def listar_produtos_cliente():
        st.header("Produtos")
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
            return

        for produto in produtos:
            categoria = View.categoria_listar_id(produto.idcategoria)
            preco_venda, promocao = View.produto_preco_venda(produto)
            col_img, col_info = st.columns([1, 3])
            with col_img:
                IndexUI.__mostrar_imagem(produto.imagem)
            with col_info:
                st.subheader(produto.descricao)
                st.write(f"Categoria: {categoria.descricao if categoria else 'Sem categoria'}")
                st.write(f"Estoque: {produto.estoque}")
                if promocao:
                    st.write(f"Promocao: {promocao.percentual:.0f}% de desconto ate {promocao.fim}")
                    st.write(f"Preco original: R$ {produto.preco:.2f}")
                    st.write(f"Preco promocional: R$ {preco_venda:.2f}")
                else:
                    st.write(f"Preco: R$ {produto.preco:.2f}")
            st.divider()

    def inserir_produto_no_carrinho():
        st.header("Inserir Produto no Carrinho")
        IndexUI.__criar_carrinho()
        produtos = [p for p in View.produto_listar() if p.estoque > 0]
        if len(produtos) == 0:
            st.write("Nenhum produto disponivel")
            return

        produto = st.selectbox("Produto", produtos)
        carrinho = st.session_state["carrinho"]
        quantidade_no_carrinho = int(carrinho.get(produto.id, 0))
        quantidade_disponivel = int(produto.estoque) - quantidade_no_carrinho
        preco_venda, promocao = View.produto_preco_venda(produto)
        IndexUI.__mostrar_imagem(produto.imagem, 220)
        st.write(f"Estoque disponivel: {produto.estoque}")
        st.write(f"No carrinho: {quantidade_no_carrinho}")
        if quantidade_disponivel <= 0:
            st.warning("Todo o estoque disponivel deste produto ja esta no carrinho")
            return
        quantidade = st.number_input("Quantidade", min_value=1, max_value=quantidade_disponivel, step=1)
        if promocao:
            st.write(f"Preco original: R$ {produto.preco:.2f}")
            st.write(f"Preco promocional: R$ {preco_venda:.2f}")
        else:
            st.write(f"Preco unitario: R$ {preco_venda:.2f}")
        if st.button("Adicionar ao carrinho"):
            try:
                quantidade_anterior = carrinho.get(produto.id, 0)
                carrinho[produto.id] = carrinho.get(produto.id, 0) + int(quantidade)
                View.carrinho_validar(carrinho)
                View.carrinho_salvar_do_cliente(st.session_state["cliente_id"], carrinho)
                st.success("Produto adicionado ao carrinho")
                st.rerun()
            except Exception as erro:
                if quantidade_anterior == 0:
                    carrinho.pop(produto.id, None)
                else:
                    carrinho[produto.id] = quantidade_anterior
                st.error(erro)

    def visualizar_carrinho():
        st.header("Carrinho")
        IndexUI.__criar_carrinho()
        carrinho = st.session_state["carrinho"]
        if len(carrinho) == 0:
            st.write("Carrinho vazio")
            return

        try:
            itens, total = View.carrinho_validar(carrinho)
            st.dataframe(IndexUI.__linhas_carrinho(itens), hide_index=True)
            st.subheader(f"Total: R$ {total:.2f}")
            if st.button("Limpar carrinho"):
                st.session_state["carrinho"] = {}
                View.carrinho_limpar_do_cliente(st.session_state["cliente_id"])
                st.rerun()
        except Exception as erro:
            st.error(erro)

    def comprar_carrinho():
        st.header("Comprar Carrinho")
        IndexUI.__criar_carrinho()
        carrinho = st.session_state["carrinho"]
        if len(carrinho) == 0:
            st.write("Carrinho vazio")
            return

        try:
            itens, total = View.carrinho_validar(carrinho)
            st.dataframe(IndexUI.__linhas_carrinho(itens), hide_index=True)
            st.subheader(f"Total: R$ {total:.2f}")
            if st.button("Confirmar compra"):
                idvenda, total = View.comprar_carrinho(st.session_state["cliente_id"], carrinho)
                st.session_state["carrinho"] = {}
                st.success(f"Compra {idvenda} realizada com sucesso. Total: R$ {total:.2f}")
                st.rerun()
        except Exception as erro:
            st.error(erro)

    def listar_compras_cliente():
        st.header("Minhas Compras")
        vendas = [v for v in View.venda_listar_por_cliente(st.session_state["cliente_id"]) if v.status == "Finalizada"]
        if len(vendas) == 0:
            st.write("Nenhuma compra realizada")
        else:
            for venda in vendas:
                entregador = View.entregador_listar_id(venda.id_entregador)
                with st.expander(f"Compra {venda.id} - {venda.data} - R$ {venda.total:.2f}"):
                    st.write(f"Status da compra: {venda.status}")
                    st.write(f"Status da entrega: {venda.status_entrega}")
                    st.write(f"Entregador: {entregador.nome if entregador else 'Aguardando alocacao'}")
                    itens = IndexUI.__itens_venda(venda.id)
                    if len(itens) == 0:
                        st.write("Nenhum item cadastrado para esta compra")
                    else:
                        st.dataframe(itens, hide_index=True)

    def __criar_carrinho():
        if "carrinho" not in st.session_state:
            if "cliente_id" in st.session_state and st.session_state.get("cliente_email") != "admin":
                st.session_state["carrinho"] = View.carrinho_obter_do_cliente(st.session_state["cliente_id"])
            else:
                st.session_state["carrinho"] = {}

    def __linhas_carrinho(itens):
        linhas = []
        for item in itens:
            produto = item["produto"]
            linha = {
                "produto": produto.descricao,
                "quantidade": item["quantidade"],
                "preco": item["preco"],
                "subtotal": item["subtotal"],
            }
            if item["promocao"]:
                linha["promocao"] = f"{item['promocao'].percentual:.0f}%"
                linha["preco_original"] = item["preco_original"]
            else:
                linha["promocao"] = ""
                linha["preco_original"] = ""
            linhas.append(linha)
        return linhas

    def __itens_venda(idvenda):
        linhas = []
        for item in View.vendaitem_listar_por_venda(idvenda):
            produto = View.produto_listar_id(item.idproduto)
            linhas.append({
                "produto": produto.descricao if produto else f"Produto {item.idproduto}",
                "quantidade": item.quantidade,
                "preco": item.preco,
                "subtotal": item.quantidade * item.preco,
            })
        return linhas

    def __data_venda(venda):
        try:
            return datetime.strptime(venda.data, "%Y-%m-%d %H:%M:%S").date()
        except ValueError:
            return date.today()

    def __mostrar_imagem(caminho, largura=160):
        if caminho and Path(caminho).exists():
            st.image(caminho, width=largura)
        else:
            st.write("Sem imagem")

    def sidebar():
        if "cliente_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            if "cliente_email" not in st.session_state:
                cliente = View.cliente_listar_id(st.session_state["cliente_id"])
                if cliente is None:
                    del st.session_state["cliente_id"]
                    del st.session_state["cliente_nome"]
                    st.rerun()
                st.session_state["cliente_email"] = cliente.email

            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            admin = st.session_state["cliente_email"] == "admin"
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            del st.session_state["cliente_email"]
            if "carrinho" in st.session_state:
                del st.session_state["carrinho"]
            st.rerun()

    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()


IndexUI.main()
