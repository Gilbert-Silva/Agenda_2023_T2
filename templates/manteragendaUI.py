import streamlit as st
import pandas as pd
from views import View
import time
import datetime

class ManterAgendaUI:
  def main():
    st.header("Cadastro de Horários")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterAgendaUI.listar()
    with tab2: ManterAgendaUI.inserir()
    with tab3: ManterAgendaUI.atualizar()
    with tab4: ManterAgendaUI.excluir()    

  def listar():
    agendas = View.agenda_listar()
    if len(agendas) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      dic = []
      for obj in agendas: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    datastr = st.text_input("Informe a data no formato *dd/mm/aaaa HH\:MM*")
    clientes = View.cliente_listar()
    cliente = st.selectbox("Selecione o cliente", clientes)
    servicos = View.servico_listar()
    servico = st.selectbox("Selecione o serviço", servicos)
    if st.button("Inserir"):
      data = datetime.datetime.strptime(datastr, "%d/%m/%Y %H:%M")
      View.agenda_inserir(data, True, cliente.get_id(), servico.get_id())
      st.success("Horário inserido com sucesso")
      time.sleep(2)
      st.rerun()

  def atualizar():
    agendas = View.agenda_listar()
    if len(agendas) == 0:
      st.write("Nenhum horário disponível")
    else:  
      op = st.selectbox("Atualização de horários", agendas)
      datastr = st.text_input("Informe a nova data no formato *dd/mm/aaaa HH\:MM*", op.get_data().strftime('%d/%m/%Y %H:%M'))
      clientes = View.cliente_listar()
      cliente_atual = View.cliente_listar_id(op.get_id_cliente())
      if cliente_atual is not None:
        cliente = st.selectbox("Selecione o novo cliente", clientes, clientes.index(cliente_atual))
      else:  
        cliente = st.selectbox("Selecione o novo cliente", clientes)
      servicos = View.servico_listar()
      servico_atual = View.servico_listar_id(op.get_id_servico())
      if servico_atual is not None:
        servico = st.selectbox("Selecione o novo serviço", servicos, servicos.index(servico_atual))
      else:
        servico = st.selectbox("Selecione o novo serviço", servicos)
      if st.button("Atualizar"):
        data = datetime.datetime.strptime(datastr, "%d/%m/%Y %H:%M")
        View.agenda_atualizar(op.get_id(), data, op.get_confirmado(), cliente.get_id(), servico.get_id())
        st.success("Horário atualizado com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    agendas = View.agenda_listar()
    if len(agendas) == 0:
      st.write("Nenhum horário disponível")
    else:  
      op = st.selectbox("Exclusão de horários", agendas)
      if st.button("Excluir"):
        View.agenda_excluir(op.get_id())
        st.success("Horário excluído com sucesso")
        time.sleep(2)
        st.rerun()


