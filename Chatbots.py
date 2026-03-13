import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="¿Puede un algoritmo entender tu tristeza?", layout="wide")

# --- ESTILOS CSS (Minimalismo y Tipografía) ---
st.markdown("""
    <style>
    /* Ocultar elementos por defecto de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Contenedor Principal */
    .main-container {
        max-width: 800px;
        margin: 0 auto;
        padding-top: 50px;
        text-align: center;
        min-height: 70vh;
    }

    /* Tipografías */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 300;
        color: #2c3e50;
        letter-spacing: -0.5px;
    }
    
    .body-text {
        font-family: 'Georgia', serif;
        font-size: 1.25rem;
        line-height: 1.8;
        color: #444;
        text-align: left;
    }

    /* Botones de Navegación */
    .stButton>button {
        border-radius: 50px;
        padding: 10px 25px;
        border: 1px solid #ddd;
        background-color: white;
        color: #555;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        border-color: #000;
        color: #000;
        background-color: #f9f9f9;
    }
    </style>
""", unsafe_allow_html=True)

# --- GESTIÓN DE ESTADO (Navegación) ---
if 'paso' not in st.session_state:
    st.session_state.paso = 0

secciones = [
    "Título", "Introducción", "Punto 1: Alianza Digital", "Punto 2: El Vínculo", 
    "Punto 3: El Secreto", "Punto 4: Roles y Calidez", "Punto 5: Personalidad", 
    "Ideas Clave", "Cierre"
]

def siguiente():
    if st.session_state.paso < len(secciones) - 1:
        st.session_state.paso += 1

def anterior():
    if st.session_state.paso > 0:
        st.session_state.paso -= 1

# --- CONTENIDO DE LAS SECCIONES ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

if st.session_state.paso == 0: # TÍTULO
    st.markdown("### ARTÍCULO DE DIVULGACIÓN")
    st.markdown("# ¿Puede un algoritmo entender tu tristeza?")
    st.markdown("#### El auge de la amistad con chatbots terapéuticos [cite: 1]")
    st.write("---")
    st.caption("La capacidad del ser humano para construir puentes de confianza y esperanza no conoce límites. [cite: 2]")

elif st.session_state.paso == 1: # INTRODUCCIÓN
    st.markdown("## ¿Conexión real o ficción?")
    st.markdown(f"""<div class="body-text">
    ¿Alguna vez has sentido que Siri o Alexa te "entienden" mejor que algunas personas? [cite: 12] 
    Para miles de personas que buscan apoyo emocional en sus teléfonos, esta conexión es una realidad tangible. [cite: 13] 
    Imagínate recibir una respuesta empática a las tres de la mañana durante una crisis de ansiedad. [cite: 14] 
    ¿Es posible generar un vínculo emocional real con un código? La ciencia actual dice que sí. [cite: 15, 16]
    </div>""", unsafe_allow_html=True)

elif st.session_state.paso == 2: # PUNTO 1
    st.markdown("## De la terapia tradicional a la 'Alianza Digital'")
    st.markdown(f"""<div class="body-text">
    En la psicología clásica, la <b>Alianza Terapéutica</b> es el "pegamento" que une al paciente con su terapeuta basado en confianza y objetivos comunes (Bordin, 1979). [cite: 18, 19]
    Hoy, hablamos de la <b>Alianza Terapéutica Digital (ATD)</b>. [cite: 20] Ya no vemos a la app como una herramienta fría, sino como una conexión subjetiva. [cite: 21, 22]
    </div>""", unsafe_allow_html=True)

elif st.session_state.paso == 3: # PUNTO 2
    st.markdown("## ¿Cómo nos 'enamora' un chatbot?")
    st.markdown(f"""<div class="body-text">
    Chatbots como <b>Woebot</b> pueden formar vínculos a "nivel humano" en tiempo récord. [cite: 25] 
    Mientras que a los humanos nos toma semanas ganar confianza, estos sistemas logran niveles de alianza similares a la terapia presencial en solo cinco días (Darcy et al., 2021). [cite: 26]
    </div>""", unsafe_allow_html=True)

elif st.session_state.paso == 4: # PUNTO 3
    st.markdown("## El Secreto: Diseño Estratégico")
    st.markdown(f"""<div class="body-text">
    No es magia. El diseño estratégico utiliza roles sociales. [cite: 27] 
    Cuando el bot asume un papel de "compañero" o "guía", las personas muestran mayor apertura emocional que con interfaces puramente técnicas (Nißen et al., 2022). [cite: 28]
    </div>""", unsafe_allow_html=True)

elif st.session_state.paso == 5: # PUNTO 4
    st.markdown("## Señales de Calidez")
    st.markdown(f"""<div class="body-text">
    El uso de emojis, la personalización del lenguaje y consejos rápidos refuerzan nuestra confianza. [cite: 29] 
    Operan en nuestras "fronteras socioemocionales", donde guardamos nuestros sentimientos más profundos (Gómez Murcia, 2024). [cite: 23]
    </div>""", unsafe_allow_html=True)

elif st.session_state.paso == 6: # PUNTO 5
    st.markdown("## Personalidad vs. Código")
    st.markdown(f"""<div class="body-text">
    No nos vinculamos con el código, sino con la "personalidad" que la IA proyecta. [cite: 30] 
    Si el sistema se siente atento, nuestro cerebro tiende a procesarlo como un apoyo real. [cite: 31]
    </div>""", unsafe_allow_html=True)

elif st.session_state.paso == 7: # IDEAS CLAVE / RIESGOS
    st.markdown("## Entre la eficacia y el riesgo")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Ventajas:** Apoyo accesible, anónimo y disponible 24/7. [cite: 34]")
    with col2:
        st.warning("**Riesgos:** Deshumanización y dependencia de un algoritmo que no puede corresponder afecto real. [cite: 36]")
    st.markdown(f"""<div class="body-text" style="font-size: 1rem;">
    Expertos advierten no confundir simulación técnica con un profesional de salud real (Corbella et al., 2025). [cite: 35]
    </div>""", unsafe_allow_html=True)

elif st.session_state.paso == 8: # CIERRE Y REFERENCIAS
    st.markdown("## El Futuro de la Alianza")
    st.markdown(f"""<div class="body-text">
    Estos "compañeros algorítmicos" ya son parte de nuestra realidad. [cite: 40] 
    El reto no es evitar el cariño hacia la tecnología, sino asegurar que esa conexión sea ética y beneficiosa. [cite: 41]
    </div>""", unsafe_allow_html=True)
    
    with st.expander("Ver Referencias Bibliográficas"):
        st.caption("Corbella, S., et al. (2025). [cite: 44]")
        st.caption("D’Alfonso, S., et al. (2020). [cite: 45]")
        st.caption("Darcy, A., et al. (2021). [cite: 46]")
        st.caption("Gómez Murcia, J. (2024). [cite: 48]")
        st.caption("Nißen, M., et al. (2022). [cite: 49]")
        st.caption("Rawat, S. (2025). [cite: 51]")
        st.caption("Vowels, L. (2024). [cite: 55]")
        st.caption("Xu, L., et al. (2025). [cite: 56]")

st.markdown('</div>', unsafe_allow_html=True)

# --- CONTROLES LATERALES ---
c1, c2, c3 = st.columns([1, 2, 1])
with c1:
    if st.session_state.paso > 0:
        st.button("← Anterior", on_click=anterior)
with c3:
    if st.session_state.paso < len(secciones) - 1:
        st.button("Siguiente →", on_click=siguiente)

# Indicador de progreso
st.progress((st.session_state.paso + 1) / len(secciones))
