import streamlit as st
from view import View


class ManterEntregaUI:
    def main():
        st.header("Controle de Entregas")
        vendas = [v for v in View.venda_listar() if v.status == "Finalizada"]
        entregadores = View.entregador_listar()
        if len(vendas) == 0:
            st.write("Nenhum pedido finalizado")
            return
        if len(entregadores) == 0:
            st.warning("Cadastre entregadores antes de controlar entregas")
            return

        venda = st.selectbox("Pedido", vendas, format_func=ManterEntregaUI.__formatar_venda)
        entregador_atual = View.entregador_listar_id(venda.id_entregador)
        st.write(f"Entregador atual: {entregador_atual.nome if entregador_atual else 'Nao alocado'}")
        st.write(f"Status atual: {venda.status_entrega}")

        indice = next((i for i, e in enumerate(entregadores) if e.id == venda.id_entregador), 0)
        entregador = st.selectbox("Entregador", entregadores, index=indice)
        status = st.selectbox(
            "Status da entrega",
            ["Aguardando alocacao", "Preparando", "Saiu para entrega", "Entregue", "Cancelada"],
            index=["Aguardando alocacao", "Preparando", "Saiu para entrega", "Entregue", "Cancelada"].index(venda.status_entrega),
        )
        if st.button("Salvar entrega"):
            try:
                View.venda_alocar_entregador(venda.id, entregador.id)
                View.venda_atualizar_status_entrega(venda.id, status)
                st.success("Entrega atualizada com sucesso")
                st.rerun()
            except Exception as erro:
                st.error(erro)

    def __formatar_venda(venda):
        cliente = View.cliente_listar_id(venda.idcliente)
        nome = cliente.nome if cliente else f"Cliente {venda.idcliente}"
        return f"Pedido {venda.id} - {nome} - R$ {venda.total:.2f}"
