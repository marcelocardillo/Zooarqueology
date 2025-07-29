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
def calcular_FD(region, bp04, bfp05, dp08, dfp07):
    coefs = coeficientes[region]
    FD = (coefs["BP04"] * bp04 +
           coefs["BFp05"] * bfp05 +
           coefs["Dp08"] * dp08 +
           coefs["DFp07"] * dfp07)
    return FD, coefs["umbral"]

# Interfaz
st.title("Clasificación de falanges de camélidos")
st.markdown("Ingrese las medidas métricas y seleccione la región para obtener la clasificación de la falange.Ingrese las medidas de la epífisis proximal de las primeras falanges (sensu Von denDriesh 1976; Kent 1982): Bp= ancho máximo de la epífisis proximal; BFp= ancho máximo de la faceta articular; Dp= profundidad máxima de la epífisis, diámetro anteroposterior; DFp= profundidad máxima de la faceta articular. Seleccione la especie (Lama glama; Lama guanicoe) y, en el caso de los guanacos, su región de procedencia para obtener la clasificación de la falange en delantera o trasera.")

region = st.selectbox("Seleccione la región / especie", list(coeficientes.keys()))

col1, col2 = st.columns(2)
with col1:
    bp04 = st.number_input("BP04 (mm)", value=0.0)
    dp08 = st.number_input("Dp08 (mm)", value=0.0)
with col2:
    bfp05 = st.number_input("BFp05 (mm)", value=0.0)
    dfp07 = st.number_input("DFp07 (mm)", value=0.0)

if st.button("Clasificar"):
    FD, umbral = calcular_FD(region, bp04, bfp05, dp08, dfp07)

    # Clasificación
    if FD < umbral:
        clasificacion = "Delantera (D)"
    elif FD > umbral:
        clasificacion = "Trasera (T)"
    else:
        clasificacion = "No diferenciada (ND)"

    # Resultado
    st.markdown(f"### Resultado")
    st.write(f"**FD = {FD:.2f}**")
    st.write(f"**Umbral de corte para {region}: {umbral}**")
    st.write(f"**Clasificación: {clasificacion}**")

    # Explicación
    st.markdown("---")
    st.markdown("#### Explicación")
    st.markdown(f"""
    El valor calculado por la función discriminante (FD) se compara con el umbral de separación
    entre falanges delanteras y traseras para la región seleccionada.

    - Si FD < umbral → **Delantera (D)**
    - Si FD > umbral → **Trasera (T)**
    - Si FD == umbral → **No diferenciada (ND)**
    """)
    st.write("Fuente:Hernández,H; Cardillo, M y Lorena, G. L´Heureux.2025.INDICE DE POSICION ANATOMICA DE LAS FALANGES DE CAMELIDOS SUDAMERICANOS. UNA VIEJA (NUEVA) DISCUSION. Contacto: Dr. Marcelo Cardillo. marcelo.cardillo@gmail.com. Bibliografía citada: Kent, J. (1982). The Domestication and Exploitation of the South America Camelids: Methods of Analysis and their Application to Circum-Lacustrine Archaeological Sites in Bolivia and Peru. Tesis Doctoral inédita, Washington University, St. Louis. Von den Driesch, A. (1976). A Guide to the Measurement of Animal Bones from Archaeological Sites. Peabody Museum of Archaeology and Ethnology, Bulletin I,Universidad de Harvard. USA.")
