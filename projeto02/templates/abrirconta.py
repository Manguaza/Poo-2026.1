import streamlit as st
import time
from view import View


class AbrirContaUI:
    def main():
        st.header("Abrir Conta")
        with st.form("abrir_conta"):
            nome = st.text_input("Nome")
            email = st.text_input("E-mail")
            fone = st.text_input("Fone")
            senha = st.text_input("Senha", type="password")
            confirmar = st.text_input("Confirmar senha", type="password")
            enviar = st.form_submit_button("Abrir conta")

        if enviar:
            try:
                if senha != confirmar:
                    raise ValueError("As senhas informadas sao diferentes")

                View.cliente_inserir(nome, email, fone, senha)
                cliente = View.cliente_autenticar(email, senha)
                st.session_state["cliente_id"] = cliente["id"]
                st.session_state["cliente_nome"] = cliente["nome"]
                st.session_state["cliente_email"] = cliente["email"]
                st.success("Conta criada com sucesso")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)
