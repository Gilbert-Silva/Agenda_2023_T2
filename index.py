from templates.inicioUI import InicioUI
from templates.equacaoUI import EquacaoUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manteragendaUI import ManterAgendaUI
import streamlit as st

class IndexUI:
  def sidebar():
      op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda"])
      if op == "Manter Clientes": ManterClienteUI.main()
      if op == "Manter Serviços": ManterServicoUI.main()
      if op == "Manter Agenda": ManterAgendaUI.main()

  def main():
    IndexUI.sidebar()
    #InicioUI.main()
    #EquacaoUI.main()
    #ManterClienteUI.main()


IndexUI.main()



