import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="¿Puede un algoritmo entender tu tristeza?", layout="wide")

# --- ESTILOS CSS ---
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.main-container {
    max-width: 800px;
    margin: 0 auto;
    padding-top: 50px;
    text-align: center;
    min-height: 70vh;
}

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

# --- ESTADO ---
if 'paso' not in st.session_state:
    st.session_state.paso = 0

secciones = [
    "Título","Introducción","Punto 1","Punto 2",
    "Punto 3","Punto 4","Punto 5","Ideas Clave","Cierre"
]

def siguiente():
    if st.session_state.paso < len(secciones) - 1:
        st.session_state.paso += 1

def anterior():
    if st.session_state.paso > 0:
        st.session_state.paso -= 1

st.markdown('<div class="main-container">', unsafe_allow_html=True)

# --- SECCIONES ---

if st.session_state.paso == 0:
    st.markdown("### ARTÍCULO DE DIVULGACIÓN")
    st.markdown("# ¿Puede un algoritmo entender tu tristeza?")
    st.markdown("#### El auge de la amistad con chatbots terapéuticos")
    st.write("---")
    st.caption("La capacidad del ser humano para construir puentes de confianza y esperanza no conoce límites.")

elif st.session_state.paso == 1:
    st.markdown("## ¿Conexión real o ficción?")
    st.markdown("""
<div class="body-text">
¿Alguna vez has sentido que Siri o Alexa te "entienden" mejor que algunas personas?
Para miles de personas que buscan apoyo emocional en sus teléfonos, esta conexión es una realidad tangible.
Imagínate recibir una respuesta empática a las tres de la mañana durante una crisis de ansiedad.
¿Es posible generar un vínculo emocional real con un código? La ciencia actual dice que sí.
</div>
""", unsafe_allow_html=True)

elif st.session_state.paso == 2:
    st.markdown("## De la terapia tradicional a la 'Alianza Digital'")
    st.markdown("""
<div class="body-text">
En la psicología clásica, la <b>Alianza Terapéutica</b> es el vínculo que une al paciente con su terapeuta
basado en confianza y objetivos comunes.
Hoy también se habla de <b>Alianza Terapéutica Digital</b>.
Ya no vemos a la app solo como una herramienta fría, sino como una conexión subjetiva con el usuario.
</div>
""", unsafe_allow_html=True)

elif st.session_state.paso == 3:
    st.markdown("## ¿Cómo nos 'enamora' un chatbot?")
    st.markdown("""
<div class="body-text">
Chatbots como <b>Woebot</b> pueden formar vínculos a nivel humano en tiempo récord.
Mientras que a los humanos nos toma semanas ganar confianza,
estos sistemas logran niveles de alianza comparables a la terapia presencial en pocos días.
</div>
""", unsafe_allow_html=True)

elif st.session_state.paso == 4:
    st.markdown("## El Secreto: Diseño Estratégico")
    st.markdown("""
<div class="body-text">
No es magia. El diseño estratégico utiliza roles sociales.
Cuando el bot asume un papel de "compañero" o "guía",
las personas muestran mayor apertura emocional que con interfaces puramente técnicas.
</div>
""", unsafe_allow_html=True)

elif st.session_state.paso == 5:
    st.markdown("## Señales de Calidez")
    st.markdown("""
<div class="body-text">
El uso de emojis, la personalización del lenguaje y los consejos rápidos
refuerzan nuestra confianza.
Estas señales operan en nuestras fronteras socioemocionales,
donde solemos guardar nuestros sentimientos más profundos.
</div>
""", unsafe_allow_html=True)

elif st.session_state.paso == 6:
    st.markdown("## Personalidad vs. Código")
    st.markdown("""
<div class="body-text">
No nos vinculamos con el código, sino con la "personalidad" que la IA proyecta.
Si el sistema se percibe atento y empático,
nuestro cerebro tiende a procesarlo como un apoyo social real.
</div>
""", unsafe_allow_html=True)

elif st.session_state.paso == 7:
    st.markdown("## Entre la eficacia y el riesgo")
    col1, col2 = st.columns(2)

    with col1:
        st.info("**Ventajas:** Apoyo accesible, anónimo y disponible 24/7.")

    with col2:
        st.warning("**Riesgos:** Deshumanización o dependencia de un algoritmo.")

    st.markdown("""
<div class="body-text" style="font-size: 1rem;">
Expertos advierten que no debe confundirse una simulación tecnológica
con la atención de un profesional de salud mental real.
</div>
""", unsafe_allow_html=True)

elif st.session_state.paso == 8:
    st.markdown("## El Futuro de la Alianza")
    st.markdown("""
<div class="body-text">
Estos "compañeros algorítmicos" ya son parte de nuestra realidad.
El reto no es evitar el cariño hacia la tecnología,
sino asegurar que esa conexión sea ética y realmente beneficiosa.
</div>
""", unsafe_allow_html=True)

    with st.expander("Ver Referencias Bibliográficas"):
        st.caption("Corbella, S., et al. (2025)")
        st.caption("D’Alfonso, S., et al. (2020)")
        st.caption("Darcy, A., et al. (2021)")
        st.caption("Gómez Murcia, J. (2024)")
        st.caption("Nißen, M., et al. (2022)")
        st.caption("Rawat, S. (2025)")
        st.caption("Vowels, L. (2024)")
        st.caption("Xu, L., et al. (2025)")

st.markdown('</div>', unsafe_allow_html=True)

# --- CONTROLES ---
c1, c2, c3 = st.columns([1,2,1])

with c1:
    if st.session_state.paso > 0:
        st.button("← Anterior", on_click=anterior)

with c3:
    if st.session_state.paso < len(secciones)-1:
        st.button("Siguiente →", on_click=siguiente)

st.progress((st.session_state.paso + 1) / len(secciones))
