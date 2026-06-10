import streamlit as st
import pandas as pd
from view import View


class ManterEntregadorUI:
    def main():
        st.header("Cadastro de Entregadores")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterEntregadorUI.listar()
        with tab2: ManterEntregadorUI.inserir()
        with tab3: ManterEntregadorUI.atualizar()
        with tab4: ManterEntregadorUI.excluir()

    def listar():
        entregadores = View.entregador_listar()
        if len(entregadores) == 0:
            st.write("Nenhum entregador cadastrado")
        else:
            st.dataframe(pd.DataFrame([e.to_json() for e in entregadores]), hide_index=True)

    def inserir():
        nome = st.text_input("Nome", key="entregador_inserir_nome")
        email = st.text_input("E-mail", key="entregador_inserir_email")
        fone = st.text_input("Fone", key="entregador_inserir_fone")
        veiculo = st.text_input("Veiculo", key="entregador_inserir_veiculo")
        if st.button("Inserir entregador"):
            try:
                View.entregador_inserir(nome, email, fone, veiculo)
                st.success("Entregador inserido com sucesso")
                st.rerun()
            except Exception as erro:
                st.error(erro)

    def atualizar():
        entregadores = View.entregador_listar()
        if len(entregadores) == 0:
            st.write("Nenhum entregador cadastrado")
        else:
            entregador = st.selectbox("Entregador", entregadores, key="entregador_atualizar_entregador")
            nome = st.text_input("Nome", entregador.nome, key="entregador_atualizar_nome")
            email = st.text_input("E-mail", entregador.email, key="entregador_atualizar_email")
            fone = st.text_input("Fone", entregador.fone, key="entregador_atualizar_fone")
            veiculo = st.text_input("Veiculo", entregador.veiculo, key="entregador_atualizar_veiculo")
            if st.button("Atualizar entregador"):
                try:
                    View.entregador_atualizar(entregador.id, nome, email, fone, veiculo)
                    st.success("Entregador atualizado com sucesso")
                    st.rerun()
                except Exception as erro:
                    st.error(erro)

    def excluir():
        entregadores = View.entregador_listar()
        if len(entregadores) == 0:
            st.write("Nenhum entregador cadastrado")
        else:
            entregador = st.selectbox("Entregador para excluir", entregadores, key="entregador_excluir_entregador")
            if st.button("Excluir entregador"):
                try:
                    View.entregador_excluir(entregador.id)
                    st.success("Entregador excluido com sucesso")
                    st.rerun()
                except Exception as erro:
                    st.error(erro)
