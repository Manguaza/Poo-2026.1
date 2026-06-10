import streamlit as st
import time
from view import View


class LoginUI:
    def main():
        st.header("Entrar no sistema")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            if c is None:
                st.error("E-mail ou senha invalidos")
            else:
                st.session_state["cliente_id"] = c["id"]
                st.session_state["cliente_nome"] = c["nome"]
                st.session_state["cliente_email"] = c["email"]
                st.success("Login realizado com sucesso")
            time.sleep(2)
            st.rerun()
