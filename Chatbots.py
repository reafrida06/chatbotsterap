import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Dashboard: Alianza Digital", layout="wide")

# --- ESTILOS CSS (Minimalismo y Tipografía) ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .main-container {
        max-width: 850px;
        margin: 0 auto;
        padding-top: 30px;
        min-height: 75vh;
    }

    /* Tipografías */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 300;
        color: #1a1a1a;
    }
    
    .body-text {
        font-family: 'Georgia', serif;
        font-size: 1.3rem;
        line-height: 1.8;
        color: #333;
        text-align: left;
    }

    /* Botones Estilizados */
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        border: 1px solid #eee;
        background-color: #fcfcfc;
    }
    </style>
""", unsafe_allow_html=True)

# --- DEFINICIÓN DE SECCIONES ---
secciones = [
    "Portada", 
    "Introducción", 
    "1. Alianza Digital", 
    "2. El Vínculo con Bots", 
    "3. Diseño Estratégico", 
    "4. Calidez Algorítmica", 
    "5. Personalidad de la IA", 
    "Ideas Clave y Riesgos", 
    "Referencias"
]

# --- DASHBOARD DE NAVEGACIÓN (SIDEBAR) ---
st.sidebar.title("Navegación")
st.sidebar.markdown("Accede directamente a cualquier sección:")
# El radio button se sincroniza con el estado del paso
seleccion_directa = st.sidebar.radio(
    "Selecciona un apartado:", 
    secciones, 
    index=st.session_state.get('paso', 0),
    key="nav_radio"
)

# Actualizar el paso basado en la selección de la barra lateral
idx_seleccionada = secciones.index(seleccion_directa)
if 'paso' not in st.session_state or st.session_state.paso != idx_seleccionada:
    st.session_state.paso = idx_seleccionada

# --- FUNCIONES DE FLECHAS ---
def siguiente():
    if st.session_state.paso < len(secciones) - 1:
        st.session_state.paso += 1

def anterior():
    if st.session_state.paso > 0:
        st.session_state.paso -= 1

# --- RENDERIZADO DE CONTENIDO ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

paso_actual = st.session_state.paso

if paso_actual == 0:
    st.markdown("### ARTÍCULO DE DIVULGACIÓN")
    st.markdown("# ¿Puede un algoritmo entender tu tristeza?")
    st.markdown("#### El auge de la amistad con chatbots terapéuticos")
    st.write("---")
    st.info("Explora cómo la tecnología está redefiniendo el apoyo emocional.")

elif paso_actual == 1:
    st.markdown("## ¿Conexión real o ficción?")
    st.markdown(f"""<div class="body-text">
    ¿Alguna vez has sentido que Siri o Alexa te entienden mejor que algunas personas? Para miles de personas que buscan apoyo emocional en sus teléfonos, esta conexión es una realidad tangible. 
    Imagina despertar a las tres de la mañana con una crisis de ansiedad y encontrar una respuesta empática inmediata. Esta es la nueva frontera de la salud mental.
    </div>""", unsafe_allow_html=True)

elif paso_actual == 2:
    st.markdown("## 1. De la terapia tradicional a la 'Alianza Digital'")
    st.markdown(f"""<div class="body-text">
    En la psicología clásica, la Alianza
