import streamlit as st
import numpy as np
import pandas as pd
from retangulo import Retangulo

class InicioUI:
    def main():
        st.header("Cálculos com Retângulo")
        b = st.text_input("Base")
        h = st.text_input("Altura")
        if st.button("Calcular"):
            r = Retangulo(float(b), float(h))
            st.write(r)
            st.write(f"Área = {r.calc_area()}")
            st.write(f"Diagonal = {r.calc_diagonal()}")
