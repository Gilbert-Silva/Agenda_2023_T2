import streamlit as st
import pandas as pd
from views import View
import time

class ManterServicoUI:
  def main():
    st.header("Cadastro de Serviços")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterServicoUI.listar()
    with tab2: ManterServicoUI.inserir()
    with tab3: ManterServicoUI.atualizar()
    with tab4: ManterServicoUI.excluir()

  def listar():
    servicos = View.servico_listar()
    if len(servicos) == 0:
      st.write("Nenhum serviço cadastrado")
    else:  
      dic = []
      for obj in servicos: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    descricao = st.text_input("Informe a descrição")
    valor = st.text_input("Informe o valor (R$)")
    duracao = st.text_input("Informe a duração (min)")
    if st.button("Inserir"):
      try:
        View.servico_inserir(descricao, float(valor), int(duracao))
        st.success("Serviço inserido com sucesso")
        time.sleep(2)
        st.rerun()
      except:
        st.error("Valor ou duração tem valores inválidos!")  

  def atualizar():
    servicos = View.servico_listar()
    if len(servicos) == 0:
      st.write("Nenhum serviço cadastrado")
    else:  
      op = st.selectbox("Atualização de Servicos", servicos)
      descricao = st.text_input("Informe a nova descrição", op.get_descricao())
      valor = st.text_input("Informe o novo valor (R$)", op.get_valor())
      duracao = st.text_input("Informe a nova duração (min)", op.get_duracao())
      if st.button("Atualizar"):
        id = op.get_id()
        View.servico_atualizar(id, descricao, float(valor), int(duracao))
        st.success("Serviço atualizado com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    servicos = View.servico_listar()
    if len(servicos) == 0:
      st.write("Nenhum serviço cadastrado")
    else:  
      op = st.selectbox("Exclusão de Servicos", servicos)
      if st.button("Excluir"):
        id = op.get_id()
        View.servico_excluir(id)
        st.success("Serviço excluído com sucesso")
        time.sleep(2)
        st.rerun()
