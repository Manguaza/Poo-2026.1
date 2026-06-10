import streamlit as st
import pandas as pd
from view import View
from datetime import date


class ManterPromocaoUI:
    def main():
        st.header("Controle de Promocoes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterPromocaoUI.listar()
        with tab2: ManterPromocaoUI.inserir()
        with tab3: ManterPromocaoUI.atualizar()
        with tab4: ManterPromocaoUI.excluir()

    def listar():
        promocoes = View.promocao_listar()
        if len(promocoes) == 0:
            st.write("Nenhuma promocao cadastrada")
        else:
            st.dataframe(pd.DataFrame([ManterPromocaoUI.__promocao_json(p) for p in promocoes]), hide_index=True)

    def inserir():
        categorias = View.categoria_listar()
        if len(categorias) == 0:
            st.warning("Cadastre uma categoria antes de cadastrar promocoes")
            return
        categoria = st.selectbox("Categoria", categorias, key="promocao_inserir_categoria")
        inicio = st.date_input("Inicio", value=date.today(), key="promocao_inserir_inicio")
        fim = st.date_input("Fim", value=date.today(), key="promocao_inserir_fim")
        percentual = st.number_input("Percentual de desconto", min_value=0.01, max_value=99.99, step=1.0, key="promocao_inserir_percentual")
        if st.button("Inserir promocao"):
            try:
                View.promocao_inserir(categoria.id, inicio, fim, percentual)
                st.success("Promocao inserida com sucesso")
                st.rerun()
            except Exception as erro:
                st.error(erro)

    def atualizar():
        promocoes = View.promocao_listar()
        categorias = View.categoria_listar()
        if len(promocoes) == 0:
            st.write("Nenhuma promocao cadastrada")
        elif len(categorias) == 0:
            st.warning("Cadastre uma categoria antes de atualizar promocoes")
        else:
            promocao = st.selectbox("Promocao", promocoes, key="promocao_atualizar_promocao")
            indice = next((i for i, c in enumerate(categorias) if c.id == promocao.idcategoria), 0)
            categoria = st.selectbox("Categoria", categorias, index=indice, key="promocao_atualizar_categoria")
            inicio = st.date_input("Inicio", value=date.fromisoformat(promocao.inicio), key="promocao_atualizar_inicio")
            fim = st.date_input("Fim", value=date.fromisoformat(promocao.fim), key="promocao_atualizar_fim")
            percentual = st.number_input("Percentual de desconto", min_value=0.01, max_value=99.99, value=float(promocao.percentual), step=1.0, key="promocao_atualizar_percentual")
            if st.button("Atualizar promocao"):
                try:
                    View.promocao_atualizar(promocao.id, categoria.id, inicio, fim, percentual)
                    st.success("Promocao atualizada com sucesso")
                    st.rerun()
                except Exception as erro:
                    st.error(erro)

    def excluir():
        promocoes = View.promocao_listar()
        if len(promocoes) == 0:
            st.write("Nenhuma promocao cadastrada")
        else:
            promocao = st.selectbox("Promocao para excluir", promocoes, key="promocao_excluir_promocao")
            if st.button("Excluir promocao"):
                try:
                    View.promocao_excluir(promocao.id)
                    st.success("Promocao excluida com sucesso")
                    st.rerun()
                except Exception as erro:
                    st.error(erro)

    def __promocao_json(promocao):
        categoria = View.categoria_listar_id(promocao.idcategoria)
        dados = promocao.to_json()
        dados["categoria"] = categoria.descricao if categoria else "Categoria nao encontrada"
        return dados
