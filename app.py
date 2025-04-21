
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Painel de Frases - Lili", layout="wide")

st.title("Painel de Frases Clínicas - Lili")

# Carregar base
df = pd.read_csv("painel_lili_frases.csv")

# Filtros
modulos = ["Todos"] + sorted(df["módulo"].dropna().unique())
tipos = ["Todos"] + sorted(df["tipo"].dropna().unique())

col1, col2 = st.columns(2)
with col1:
    filtro_modulo = st.selectbox("Filtrar por módulo", modulos)
with col2:
    filtro_tipo = st.selectbox("Filtrar por tipo", tipos)

# Aplicar filtros
df_filtrado = df.copy()
if filtro_modulo != "Todos":
    df_filtrado = df_filtrado[df_filtrado["módulo"] == filtro_modulo]
if filtro_tipo != "Todos":
    df_filtrado = df_filtrado[df_filtrado["tipo"] == filtro_tipo]

# Busca
busca = st.text_input("Buscar por palavra-chave").lower()
if busca:
    df_filtrado = df_filtrado[df_filtrado.apply(lambda row: busca in row.astype(str).str.lower().to_string(), axis=1)]

# Mostrar tabela
st.dataframe(df_filtrado, use_container_width=True)

# Download
st.download_button("📥 Baixar CSV Atual", df_filtrado.to_csv(index=False), "frases_lili_atual.csv", "text/csv")
