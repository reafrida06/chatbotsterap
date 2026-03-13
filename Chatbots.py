import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Dashboard: Alianza Digital", layout="wide")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .main-container {
        max-width: 850px;
        margin: 0 auto;
        padding-top: 30px;
        min-height: 70vh;
    }

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

# --- GESTIÓN DE ESTADO ---
if 'paso' not in st.session_state:
    st.session_state.paso = 0

# --- DASHBOARD LATERAL (SIDEBAR) ---
st.sidebar.title("Navegación")
# El radio button controla el estado global
seleccion = st.sidebar.radio(
    "Ir directamente a:", 
    secciones, 
    index=st.session_state.paso
)

# Actualizar el paso si el usuario usa el radio de la barra lateral
st.session_state.paso = secciones.index(seleccion)

# --- FUNCIONES DE NAVEGACIÓN (BOTONES) ---
def siguiente():
    if st.session_state.paso < len(secciones) - 1:
        st.session_state.paso += 1

def anterior():
    if st.session_state.paso > 0:
        st.session_state.paso -= 1

# --- RENDERIZADO DE CONTENIDO ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

p = st.session_state.paso

if p == 0:
    st.markdown("### ARTÍCULO DE DIVULGACIÓN")
    st.markdown("# ¿Puede un algoritmo entender tu tristeza?")
    st.markdown("#### El auge de la amistad con chatbots terapéuticos")
    st.write("---")
    st.info("Explora cómo la tecnología intenta cerrar la brecha en salud mental.")

elif p == 1:
    st.markdown("## ¿Conexión real o ficción?")
    st.markdown('<div class="body-text">¿Siri o Alexa te entienden mejor que algunas personas? Para miles de personas que buscan apoyo emocional en sus teléfonos, esta conexión es una realidad tangible. Imagina despertar a las tres de la mañana con una crisis de ansiedad y recibir una respuesta empática de un asistente virtual.</div>', unsafe_allow_html=True)

elif p == 2:
    st.markdown("## 1. De la terapia tradicional a la Alianza Digital")
    st.markdown('<div class="body-text">En la psicología clásica, la Alianza Terapéutica es el pegamento que une al paciente con su terapeuta basado en la confianza mutua. Con la evolución tecnológica, surge la Alianza Terapéutica Digital (ATD), donde establecemos una conexión subjetiva con la aplicación que predice el éxito del proceso.</div>', unsafe_allow_html=True)

elif p == 3:
    st.markdown("## 2. El Vínculo con los Bots")
    st.markdown('<div class="body-text">Chatbots como Woebot pueden formar vínculos a nivel humano en tiempo récord. Mientras que a los humanos nos toma semanas ganar confianza, estos sistemas logran niveles de alianza similares a la terapia presencial en solo cinco días.</div>', unsafe_allow_html=True)

elif p == 4:
    st.markdown("## 3. El Secreto: Diseño Estratégico")
    st.markdown('<div class="body-text">No es magia, es diseño
