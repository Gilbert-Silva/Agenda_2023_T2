import streamlit as st
import pandas as pd
from views import View
import time
import datetime

class AgendaHojeUI:
  def main():
    st.header("Agenda de Hoje")
    AgendaHojeUI.listar()

  def listar():
    agendas = View.agenda_listarhoje()
    if len(agendas) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      dic = []
      for obj in agendas: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)