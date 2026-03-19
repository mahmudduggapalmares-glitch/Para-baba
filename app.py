import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(page_title="Feliz Día del Padre", page_icon="🚀", layout="centered")

# Estilo personalizado para el "Espacio"
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .main-title {
        font-size: 3rem;
        text-align: center;
        color: #FFD700;
        text-shadow: 2px 2px 4px #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 1. Música de Fondo (Autoplay)
# Usamos un iframe oculto para la canción "Mi Viejo" de Piero
st.write("### 🎵 Escuchando: Mi Viejo - Piero")
components.html(
    """
    <iframe width="0" height="0" src="https://www.youtube.com/embed/soRmpPJOIwo?autoplay=1&loop=1" 
    frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    """,
    height=0,
)

# 2. Título y Mensaje Principal
st.markdown('<h1 class="main-title">🚀 ¡Feliz Día del Padre! 🌌</h1>', unsafe_allow_html=True)
st.write("---")
st.balloons() # Efecto visual de celebración

st.subheader("Para el mejor papá del mundo:")
st.write(
    """
    Papá, en este pequeño rincón del universo digital, quiero decirte que eres y siempre serás 
    **el mejor papá del mundo**. No hay nadie como tú, tu fuerza y tu cariño son mi guía.
    """
)

# 3. Temática de Juegos: "Trivia de Superpapá"
st.sidebar.header("🕹️ Zona de Juegos")
juego = st.sidebar.radio("Elige un juego:", ["Trivia de Papá", "Mensaje Estelar"])

if juego == "Trivia de Papá":
    st.write("### 🧠 ¿Cuánto sabes de tu hijo/a?")
    pregunta = st.radio("¿Cuál es nuestro recuerdo favorito juntos?", 
                        ["Viajes", "Nuestras charlas", "Cuando cocinamos", "Todo el tiempo juntos"])
    if st.button("Verificar"):
        st.success(f"¡Correcto! Porque {pregunta.lower()} es lo que nos hace únicos. ¡Eres el mejor!")

elif juego == "Mensaje Estelar":
    st.write("### ✨ Generador de Elogios")
    if st.button("Haz clic para una verdad estelar"):
        frases = [
            "Eres mi héroe sin capa.",
            "No hay galaxia con un padre tan genial como tú.",
            "Tu sabiduría es más grande que el universo.",
            "Eres el pilar de nuestra familia."
        ]
        import random
        st.info(random.choice(frases))

# Pie de página
st.markdown("---")
st.write("✨ *Creado con mucho amor para el hombre más importante.*")

