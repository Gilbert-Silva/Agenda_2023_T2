import streamlit as st
import pandas as pd
from views import View
import time

class ServicoReajusteUI:
  def main():
    st.header("Reajuste de Preço")
    ServicoReajusteUI.listar()


  def listar():
    servicos = View.servico_listar()
    if len(servicos) == 0:
      st.write("Nenhum serviço cadastrado")
    else:  
      dic = []
      for obj in servicos: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)
      percentual = st.text_input("Informe o percentual (%)")
      if st.button("Reajustar"):
        View.servico_reajustar(float(percentual))
        st.success("Reajuste realizado com sucesso")
        time.sleep(2)
        st.rerun() 