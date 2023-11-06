from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manteragendaUI import ManterAgendaUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.loginUI import LoginUI
from templates.agendahojeUI import AgendaHojeUI
from templates.servicoreajusteUI import ServicoReajusteUI
from templates.abrircontaUI import AbrirContaUI
from views import View

import streamlit as st

class IndexUI:
      
    def sidebar():
      op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda", "Abrir Agenda do Dia", "Login", "Agenda de Hoje", "Reajuste de Preço", "Abrir Conta"])
      if op == "Manter Clientes": ManterClienteUI.main()
      if op == "Manter Serviços": ManterServicoUI.main()
      if op == "Manter Agenda": ManterAgendaUI.main()
      if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
      if op == "Login": LoginUI.main()
      if op == "Agenda de Hoje": AgendaHojeUI.main()
      if op == "Reajuste de Preço": ServicoReajusteUI.main()
      if op == "Abrir Conta": AbrirContaUI.main()

      if "cliente_id" in st.session_state:
        st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
      else:   
        st.sidebar.write("Nenhum usuário entrou no sistema")
        
      #if op == "Manter Clientes": st.session_state["page"] = "manter_clienteUI"

    def main():
      View.cliente_admin()
      IndexUI.sidebar()

      #if "page" not in st.session_state: st.session_state["page"] = "equacaoUI"
      #if st.session_state["page"] == "manter_clienteUI": ManterClienteUI.main()

IndexUI.main()



