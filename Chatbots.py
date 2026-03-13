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
        min-height: 75vh;
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

# --- DASHBOARD LATERAL ---
st.sidebar.title("Navegación")
# Sincronizamos el radio button con el estado actual
seleccion = st.sidebar.radio(
    "Ir a:", 
    secciones, 
    index=st.session_state.paso,
    key="nav_radio"
)

# Si el usuario cambia manualmente en el sidebar, actualizamos el paso
st.session_state.paso = secciones.index(seleccion)

# --- FUNCIONES DE NAVEGACIÓN ---
def siguiente():
    if st.session_state.paso < len(secciones) - 1:
        st.session_state.paso += 1

def anterior():
    if st.session_state.paso > 0:
        st.session_state.paso -= 1

# --- CONTENIDO ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

p = st.session_state.paso

if p == 0:
    st.markdown("### ARTÍCULO DE DIVULGACIÓN")
    st.markdown("# ¿Puede un algoritmo entender tu tristeza?")
    st.markdown("#### El auge de la amistad con chatbots terapéuticos")
    st.write("---")
    st.info("Explora cómo la tecnología está redefiniendo el apoyo emocional.")

elif p == 1:
    st.markdown("## ¿Conexión real o ficción?")
    st.markdown('<div class="body-text">¿Alguna vez has sentido que Siri o Alexa te entienden mejor que algunas personas? Para miles de personas que buscan apoyo emocional en sus teléfonos, esta conexión es una realidad tangible. Imagina despertar a las tres de la mañana con una crisis de ansiedad y encontrar una respuesta empática inmediata. Esta es la nueva frontera de la salud mental.</div>', unsafe_allow_html=True)

elif p == 2:
    st.markdown("## 1. De la terapia tradicional a la Alianza Digital")
    st.markdown('<div class="body-text">En la psicología clásica, la Alianza Terapéutica es el pegamento que une al paciente con su terapeuta. Hoy, la Alianza Terapéutica Digital (ATD) propone que no vemos a la aplicación solo como una herramienta, sino como un agente con el que establecemos una conexión subjetiva y metas comunes.</div>', unsafe_allow_html=True)

elif p == 3:
    st.markdown("## 2. El Vínculo con los Bots")
    st.markdown('<div class="body-text">Chatbots como Woebot han demostrado que pueden formar vínculos de confianza a un nivel casi humano en tiempo récord. A diferencia de la terapia presencial que requiere semanas de contacto, estos sistemas logran establecer una alianza sólida en apenas pocos días de interacción constante.</div>', unsafe_allow_html=True)

elif p == 4:
    st.markdown("## 3. El Secreto: Diseño Estratégico")
    st.markdown('<div class="body-text">No es solo código; es diseño social. Cuando un chatbot asume un rol claro, como ser un compañero o un guía, los usuarios tienden a abrirse emocionalmente con mayor facilidad. Esta estructura reduce la fricción y fomenta una comunicación más honesta.</div>', unsafe_allow_html=True)

elif p == 5:
    st.markdown("## 4. Señales de Calidez Algorítmica")
    st.markdown('<div class="body-text">Pequeños detalles como el uso de emojis, la personalización de las respuestas y la disponibilidad inmediata actúan como señales de calidez. Estos elementos operan en nuestras fronteras socioemocionales, permitiéndonos confiar nuestros sentimientos más profundos a una entidad digital.</div>', unsafe_allow_html=True)

elif p == 6:
    st.markdown("## 5. Personalidad de la IA")
    st.markdown('<div class="body-text">Nuestro cerebro suele procesar la interactividad de la IA como si fuera una interacción humana. Al proyectar una personalidad atenta y receptiva, el algoritmo deja de ser un programa para convertirse en un apoyo percibido como real por nuestra psique.</div>', unsafe_allow_html=True)

elif p == 7:
    st.markdown("## Ideas Clave y Riesgos")
    st.markdown('<div class="body-text">Aunque la accesibilidad 24/7 es una ventaja revolucionaria, existen riesgos importantes como la deshumanización (el peligro de sustituir el contacto humano real por simulaciones) y la dependencia hacia sistemas que no poseen conciencia afectiva real.</div>', unsafe_allow_html=True)

elif p == 8:
    st.markdown("## Referencias Bibliográficas")
    st.caption("Fuentes consultadas:")
    st.markdown("- Corbella, S., et al. (2025)\n- Darcy, A., et al. (2021)\n- Nißen, M., et al. (2022)\n- Vowels, L. (2024)")

st.
