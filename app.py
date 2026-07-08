import random
import streamlit as st

st.set_page_config(
    page_title="Código de Honor · Contadeus International",
    page_icon="🏅",
    layout="centered",
)

# ----------------------------
# Contenido
# ----------------------------
RULES = [
    {"title": "Comunicación", "text": "Aprovecha cada oportunidad para estar en contacto. ¡Todos somos vendedores!"},
    {"title": "Éxito y celebración", "text": "Haz todo lo posible para tener éxito y celebra todos los logros."},
    {"title": "Trabajo en equipo", "text": "Estar siempre dispuesto a ayudar al compañero de equipo."},
    {"title": "Responsabilidad", "text": "Sé responsable: no niegues, no culpes a otros y no te justifiques."},
    {"title": "Disciplina", "text": "Orden y un registro fiel del debe y el haber."},
    {"title": "Dudas y observaciones", "text": "Cuando tengas dudas, ¡pregunta! Cuando encuentres observaciones, ¡informa!"},
    {"title": "Puntualidad", "text": "Sé puntual y trabaja primero en lo más importante, con base en la planificación."},
    {"title": "Eficiencia", "text": "Aprovecha al máximo la tecnología para hacer más con menos."},
    {"title": "Concentración", "text": "Concéntrate en lo que haces y en las metas para tener grandes resultados."},
    {"title": "Aprendizaje continuo", "text": "Sigue aprendiendo y recuerda enseñar lo que sabes a los demás."},
    {"title": "Actitud positiva", "text": "No critiques, no condenes y no te quejes."},
]

MISSION = (
    "Elevar a las personas para que lideren sus negocios con claridad financiera, "
    "equipos sólidos y crecimiento constante."
)
VISION = "Mil líderes con claridad en sus negocios."

EXTRA_QUESTIONS = [
    {
        "q": "¿Cuál es la misión de Contadeus International?",
        "correct": MISSION,
        "wrongs": [
            "Ser la firma contable más grande de la región.",
            "Vender software de contabilidad a bajo costo.",
            "Capacitar contadores en normas internacionales.",
        ],
    },
    {
        "q": "¿Cuál es la visión de Contadeus International?",
        "correct": VISION,
        "wrongs": [
            "Abrir mil oficinas en Latinoamérica.",
            "Ser reconocidos como la mejor firma de auditoría.",
            "Mil clientes satisfechos cada año.",
        ],
    },
]

# ----------------------------
# Estilos simples
# ----------------------------
st.markdown(
    """
    <style>
    .card {
        background: #ffffff;
        border: 1px solid #e5e5e5;
        border-radius: 16px;
        padding: 2rem 1.5rem;
        text-align: center;
        min-height: 160px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        margin-bottom: 1rem;
    }
    .card h3 { margin: 0; font-size: 1.4rem; }
    .card p { margin: 0; font-size: 1.05rem; color: #444; }
    .mv-card {
        background: #f7f7fb;
        border-left: 5px solid #4A47D5;
        border-radius: 10px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
    }
    .mv-card h4 { margin: 0 0 0.4rem 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🏅 Código de Honor")
st.caption("Contadeus International")

tab1, tab2, tab3 = st.tabs(["📇 Tarjetas", "🎯 Misión y visión", "🧠 Quiz rápido"])

# ----------------------------
# TAB 1: Tarjetas (flashcards)
# ----------------------------
with tab1:
    if "card_idx" not in st.session_state:
        st.session_state.card_idx = 0
    if "flipped" not in st.session_state:
        st.session_state.flipped = False

    idx = st.session_state.card_idx
    rule = RULES[idx]

    st.write(f"Regla **{idx + 1}** de **{len(RULES)}**")

    if st.session_state.flipped:
        st.markdown(f'<div class="card"><p>{rule["text"]}</p></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="card"><h3>{idx + 1}. {rule["title"]}</h3></div>', unsafe_allow_html=True)

    if st.button("🔄 Voltear tarjeta", use_container_width=True):
        st.session_state.flipped = not st.session_state.flipped
        st.rerun()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Anterior", use_container_width=True):
            st.session_state.card_idx = (idx - 1) % len(RULES)
            st.session_state.flipped = False
            st.rerun()
    with col2:
        if st.button("Siguiente ➡️", use_container_width=True):
            st.session_state.card_idx = (idx + 1) % len(RULES)
            st.session_state.flipped = False
            st.rerun()

# ----------------------------
# TAB 2: Misión y visión
# ----------------------------
with tab2:
    st.markdown(
        f'<div class="mv-card"><h4>🎯 Misión</h4><p>{MISSION}</p></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="mv-card"><h4>🔭 Visión</h4><p>{VISION}</p></div>',
        unsafe_allow_html=True,
    )

# ----------------------------
# TAB 3: Quiz
# ----------------------------
with tab3:

    def build_quiz():
        rule_indices = random.sample(range(len(RULES)), 6)
        rule_questions = []
        for i in rule_indices:
            wrong_pool = [r["title"] for j, r in enumerate(RULES) if j != i]
            wrongs = random.sample(wrong_pool, 3)
            rule_questions.append(
                {"q": RULES[i]["text"], "correct": RULES[i]["title"], "wrongs": wrongs}
            )
        items = rule_questions + EXTRA_QUESTIONS
        random.shuffle(items)
        for item in items:
            options = item["wrongs"] + [item["correct"]]
            random.shuffle(options)
            item["options"] = options
        return items

    if "quiz_items" not in st.session_state:
        st.session_state.quiz_items = build_quiz()
        st.session_state.q_idx = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.chosen = None

    def restart_quiz():
        st.session_state.quiz_items = build_quiz()
        st.session_state.q_idx = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.chosen = None

    items = st.session_state.quiz_items
    q_idx = st.session_state.q_idx

    if q_idx < len(items):
        item = items[q_idx]
        st.write(f"Pregunta **{q_idx + 1}** de **{len(items)}**  ·  Aciertos: **{st.session_state.score}**")
        st.markdown(f"**{item['q']}**")

        if not st.session_state.answered:
            for opt in item["options"]:
                if st.button(opt, key=f"{q_idx}-{opt}", use_container_width=True):
                    st.session_state.answered = True
                    st.session_state.chosen = opt
                    if opt == item["correct"]:
                        st.session_state.score += 1
                    st.rerun()
        else:
            for opt in item["options"]:
                if opt == item["correct"]:
                    st.success(opt)
                elif opt == st.session_state.chosen:
                    st.error(opt)
                else:
                    st.write(opt)

            if st.button("Siguiente pregunta ➡️", use_container_width=True):
                st.session_state.q_idx += 1
                st.session_state.answered = False
                st.session_state.chosen = None
                st.rerun()
    else:
        pct = st.session_state.score / len(items)
        st.subheader(f"Resultado: {st.session_state.score} de {len(items)} correctas")
        if pct == 1:
            st.balloons()
            st.write("Excelente, dominas el código, la misión y la visión.")
        elif pct >= 0.6:
            st.write("Buen trabajo, repasa lo que fallaste en la sección de tarjetas.")
        else:
            st.write("Vale la pena repasar las tarjetas de nuevo antes de reintentar.")

        if st.button("🔁 Reintentar quiz", use_container_width=True):
            restart_quiz()
            st.rerun()
