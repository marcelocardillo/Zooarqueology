import streamlit as st

# Diccionario con coeficientes por región
coeficientes = {
    "Lama glama": {
        "BP04": -0.6541918,
        "BFp05": 0.5418537,
        "Dp08": -0.7494701,
        "DFp07": -0.5538084,
        "umbral": -27.23
    },
    "Lama guanicoe NOA": {
        "BP04": 0.36807501,
        "BFp05": -0.08692864,
        "Dp08": -1.17219650,
        "DFp07": -0.63132924,
        "umbral": -28.33
    },
    "Lama guanicoe Norpatagonia": {
        "BP04": -0.2095383,
        "BFp05": 0.0279237,
        "Dp08": 0.1569139,
        "DFp07": -1.4109877,
        "umbral": -28.27
    },
    "Lama guanicoe Patagonia Austral": {
        "BP04": 0.6295074,
        "BFp05": -0.2799106,
        "Dp08": 0.1728613,
        "DFp07": -1.6661510,
        "umbral": -21.54
    }
}

# Función para calcular el valor discriminante
def calcular_ld1(region, bp04, bfp05, dp08, dfp07):
    coefs = coeficientes[region]
    ld1 = (coefs["BP04"] * bp04 +
           coefs["BFp05"] * bfp05 +
           coefs["Dp08"] * dp08 +
           coefs["DFp07"] * dfp07)
    return ld1, coefs["umbral"]

# Interfaz
st.title("Clasificación de falanges de camélidos")
st.markdown("Ingrese las medidas métricas y seleccione la región para obtener la clasificación de la falange.")

region = st.selectbox("Seleccione la región / especie", list(coeficientes.keys()))

col1, col2 = st.columns(2)
with col1:
    bp04 = st.number_input("BP04 (mm)", value=0.0)
    dp08 = st.number_input("Dp08 (mm)", value=0.0)
with col2:
    bfp05 = st.number_input("BFp05 (mm)", value=0.0)
    dfp07 = st.number_input("DFp07 (mm)", value=0.0)

if st.button("Calcular clasificación"):
    ld1, umbral = calcular_ld1(region, bp04, bfp05, dp08, dfp07)

    # Clasificación
    if ld1 < umbral:
        clasificacion = "Delantera (D)"
    elif ld1 > umbral:
        clasificacion = "Trasera (T)"
    else:
        clasificacion = "No diferenciada (ND)"

    # Resultado
    st.markdown(f"### Resultado")
    st.write(f"**LD1 = {ld1:.2f}**")
    st.write(f"**Umbral de corte para {region}: {umbral}**")
    st.write(f"**Clasificación: {clasificacion}**")

    # Explicación
    st.markdown("---")
    st.markdown("#### Explicación")
    st.markdown(f"""
    El valor calculado de la función discriminante (LD1) se compara con el umbral de separación
    entre falanges delanteras y traseras para la región seleccionada.

    - Si LD1 < umbral → **Delantera (D)**
    - Si LD1 > umbral → **Trasera (T)**
    - Si LD1 == umbral → **No diferenciada (ND)**
    """)
    st.write("Fuente:Hernández,H; Cardillo, M y Lorena, G. L’Heureux.2025
INDICE DE POSICION ANATOMICA DE LAS FALANGES DE CAMELIDOS SUDAMERICANOS. UNA VIEJA (NUEVA) DISCUSION. Contacto: Dr. Marcelo Cardillo. marcelo.cardillo@gmail.com")
