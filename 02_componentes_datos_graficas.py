import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

@st.cache_data
def load_data(filename):
    data = pd.read_csv(filename)
    return data

df = load_data("subsidios.csv")

st.title("Componentes de datos")

st.subheader("Dataframe")

st.dataframe(df)

st.subheader("Tabla")

st.table(df)

st.subheader("Métrica")

st.metric(label="PIB", value="1.076 B", delta="-1.5 %")

#gráfica de dispersión
st.scatter_chart(data=df,x="Becas_Hombres", y="Becas_Mujeres", use_container_width=True)

#gráfica de pastel
becas_hombres = df.groupby('Nivel')['Becas_Hombres'].sum()
fig, ax = plt.subplots()
ax.pie(becas_hombres, labels= becas_hombres.index, autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(fig)

#gráfica de barras agrupadas
df_grouped = df.groupby('Nivel', as_index=False)[['Becas_Hombres', 'Becas_Mujeres']].sum()

niveles = df_grouped['Nivel']
x = np.arange(len(niveles))
ancho = 0.35

fig, ax = plt.subplots()

# Barras de hombres
ax.bar(x - ancho/2, df_grouped['Becas_Hombres'], width=ancho, label='Hombres', color='#1f77b4')

# Barras de mujeres
ax.bar(x + ancho/2, df_grouped['Becas_Mujeres'], width=ancho, label='Mujeres', color='#ea899a')

# Etiquetas y detalles
ax.set_xlabel('Nivel')
ax.set_ylabel('Monto Total Otorgado ($)')
ax.set_title('Monto Total Otorgado por Nivel y Género')
ax.set_xticks(x)
ax.set_xticklabels(niveles)
ax.legend()

# Mostrar en Streamlit
st.write("Monto Total Otorgado por Nivel y Género")
st.pyplot(fig)

'''
st.subheader("JSON")

diccionario = {
    "created_at": "Wed Oct 10 20:19:24 +0000 2018",
    "id": 1050118621198921728,
    "id_str": "1050118621198921728",
    "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
    "user": {},  
    "entities": {}
}

st.json(diccionario)'''
