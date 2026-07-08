import random
import streamlit as st

st.set_page_config(
    page_title="Código de Honor · Contadeus International",
    page_icon="🏅",
    layout="centered",
)

# ============================================================
# CONTENIDO
# ============================================================
RULES = [
    # "text" = redacción exacta del PDF original (para tarjetas).
    # "quiz_text" = misma idea sin la palabra clave inicial, para que el quiz no regale la respuesta.
    {"title": "Comunicación", "text": "Comunicación, aprovecha cada oportunidad para estar en contacto ¡todos somos vendedores!",
     "quiz_text": "Aprovecha cada oportunidad para estar en contacto ¡todos somos vendedores!"},
    {"title": "Éxito y celebración", "text": "Haz todo lo posible para tener éxito y celebra todos los logros.",
     "quiz_text": "Haz todo lo posible para tener éxito y celebra todos los logros."},
    {"title": "Trabajo en equipo", "text": "Trabajo en equipo, estar siempre dispuesto a ayudar al compañero de equipo.",
     "quiz_text": "Estar siempre dispuesto a ayudar al compañero de equipo."},
    {"title": "Responsabilidad", "text": "Sé responsable, no niegues, no culpes a otros y no te justifiques.",
     "quiz_text": "No niegues, no culpes a otros y no te justifiques."},
    {"title": "Disciplina", "text": "Disciplina, orden y un registro fiel del debe y el haber.",
     "quiz_text": "Orden y un registro fiel del debe y el haber."},
    {"title": "Dudas y observaciones", "text": "Cuando tengas dudas ¡Pregunta! Cuando encuentres observaciones ¡Informa!",
     "quiz_text": "Cuando tengas dudas ¡Pregunta! Cuando encuentres observaciones ¡Informa!"},
    {"title": "Puntualidad", "text": "Sé puntual y trabaja primero en lo más importante teniendo como base la planificación.",
     "quiz_text": "Trabaja primero en lo más importante teniendo como base la planificación."},
    {"title": "Eficiencia", "text": "Eficiencia, aprovecha al máximo la tecnología para hacer más con menos.",
     "quiz_text": "Aprovecha al máximo la tecnología para hacer más con menos."},
    {"title": "Concentración", "text": "Concéntrate en lo que haces y en las metas para tener grandes resultados.",
     "quiz_text": "Concéntrate en lo que haces y en las metas para tener grandes resultados."},
    {"title": "Aprendizaje continuo", "text": "Sigue en continuo aprendizaje y recuerda en enseñar lo que sabes a los demás.",
     "quiz_text": "Sigue en continuo aprendizaje y recuerda en enseñar lo que sabes a los demás."},
    {"title": "Actitud positiva", "text": "No critiques, no condenes y no te quejes.",
     "quiz_text": "No critiques, no condenes y no te quejes."},
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

# "Completa la frase": cada ítem tiene la oración con un espacio en blanco
# y 4 opciones (incluida la correcta) para elegir la palabra/frase que falta.
FILL_BLANKS = [
    {"sentence": "_____, aprovecha cada oportunidad para estar en contacto ¡todos somos vendedores!",
     "answer": "Comunicación", "options": ["Comunicación", "Disciplina", "Eficiencia", "Puntualidad"]},
    {"sentence": "Haz todo lo posible para tener _____ y celebra todos los logros.",
     "answer": "éxito", "options": ["éxito", "paciencia", "calma", "dinero"]},
    {"sentence": "_____, estar siempre dispuesto a ayudar al compañero de equipo.",
     "answer": "Trabajo en equipo", "options": ["Trabajo en equipo", "Responsabilidad", "Concentración", "Disciplina"]},
    {"sentence": "Sé responsable, no niegues, no culpes a otros y no te _____.",
     "answer": "justifiques", "options": ["justifiques", "enojes", "apures", "distraigas"]},
    {"sentence": "_____, orden y un registro fiel del debe y el haber.",
     "answer": "Disciplina", "options": ["Disciplina", "Eficiencia", "Puntualidad", "Comunicación"]},
    {"sentence": "Cuando tengas dudas ¡_____! Cuando encuentres observaciones ¡Informa!",
     "answer": "Pregunta", "options": ["Pregunta", "Espera", "Adivina", "Ignora"]},
    {"sentence": "Sé puntual y trabaja primero en lo más importante teniendo como base la _____.",
     "answer": "planificación", "options": ["planificación", "suerte", "memoria", "costumbre"]},
    {"sentence": "_____, aprovecha al máximo la tecnología para hacer más con menos.",
     "answer": "Eficiencia", "options": ["Eficiencia", "Disciplina", "Responsabilidad", "Comunicación"]},
    {"sentence": "_____ en lo que haces y en las metas para tener grandes resultados.",
     "answer": "Concéntrate", "options": ["Concéntrate", "Apúrate", "Relájate", "Distráete"]},
    {"sentence": "Sigue en continuo _____ y recuerda en enseñar lo que sabes a los demás.",
     "answer": "aprendizaje", "options": ["aprendizaje", "descanso", "silencio", "trabajo"]},
    {"sentence": "No critiques, no condenes y no te _____.",
     "answer": "quejes", "options": ["quejes", "rías", "calles", "apresures"]},
]

# "Caso del día": mini escenarios reales, cada uno mapeado a una regla del código.
CASES = [
    {"scenario": "Un cliente te escribe por WhatsApp preguntando por el estado de su trámite. Según el código, ¿qué deberías hacer?",
     "rule": "Comunicación"},
    {"scenario": "Tu equipo logró cerrar un contrato importante después de varias semanas de trabajo. ¿Qué principio del código aplica aquí?",
     "rule": "Éxito y celebración"},
    {"scenario": "Un compañero está saturado de trabajo y tú ya terminaste tus pendientes del día. ¿Qué dicta el código de honor?",
     "rule": "Trabajo en equipo"},
    {"scenario": "Cometiste un error en un reporte y el cliente lo notó. ¿Cuál es la actitud correcta según el código?",
     "rule": "Responsabilidad"},
    {"scenario": "Al cierre del mes notas que tus registros contables tienen desorden. ¿Qué principio no estás cumpliendo?",
     "rule": "Disciplina"},
    {"scenario": "No entiendes bien un procedimiento nuevo de la empresa. ¿Qué deberías hacer según el código?",
     "rule": "Dudas y observaciones"},
    {"scenario": "Tienes una reunión importante a las 9am y también correos pendientes de responder. ¿Qué prioriza el código?",
     "rule": "Puntualidad"},
    {"scenario": "Podrías automatizar una tarea repetitiva con una herramienta digital, pero prefieres seguir haciéndola manualmente. ¿Qué dice el código?",
     "rule": "Eficiencia"},
    {"scenario": "Estás en medio de una tarea importante pero las notificaciones del celular no paran de sonar. ¿Qué recomienda el código?",
     "rule": "Concentración"},
    {"scenario": "Aprendiste una nueva forma de hacer un trámite más rápido. Según el código, ¿qué deberías hacer con ese conocimiento?",
     "rule": "Aprendizaje continuo"},
    {"scenario": "Un compañero cometió un error que te generó más trabajo. ¿Cuál es la actitud correcta según el código?",
     "rule": "Actitud positiva"},
]

# Quiz Verdadero/Falso sobre Misión y Visión.
MV_STATEMENTS = [
    {"text": "La misión de Contadeus International es elevar a las personas para que lideren sus negocios con claridad financiera, equipos sólidos y crecimiento constante.", "is_true": True},
    {"text": "La visión de Contadeus International es tener mil líderes con claridad en sus negocios.", "is_true": True},
    {"text": "La misión de Contadeus International es ser la firma de auditoría más grande de la región.", "is_true": False},
    {"text": "La visión busca abrir mil oficinas físicas en Latinoamérica.", "is_true": False},
    {"text": "Parte de la misión incluye ayudar a formar equipos sólidos dentro de los negocios de los clientes.", "is_true": True},
    {"text": "La visión se enfoca en la cantidad de clientes atendidos, no en líderes formados.", "is_true": False},
    {"text": "La misión menciona el crecimiento constante como parte de lo que se busca para las personas.", "is_true": True},
    {"text": "La visión habla de mil empleados contratados, no de mil líderes.", "is_true": False},
]

# ============================================================
# ESTILOS
# ============================================================
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
    .case-box {
        background: #fff8ec;
        border-left: 5px solid #E5A100;
        border-radius: 10px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
        font-size: 1.02rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🏅 Código de Honor")
st.caption("Contadeus International")

# ============================================================
# HELPER GENÉRICO PARA QUIZZES DE OPCIÓN MÚLTIPLE
# ============================================================
def run_mcq(key_prefix, build_fn, mastery_msg="¡Excelente! Nivel dominado.",
            good_msg="Buen trabajo, repasa lo que fallaste.",
            low_msg="Vale la pena repasar el material antes de reintentar."):
    items_key = f"{key_prefix}_items"
    idx_key = f"{key_prefix}_idx"
    score_key = f"{key_prefix}_score"
    answered_key = f"{key_prefix}_answered"
    chosen_key = f"{key_prefix}_chosen"

    def start():
        st.session_state[items_key] = build_fn()
        st.session_state[idx_key] = 0
        st.session_state[score_key] = 0
        st.session_state[answered_key] = False
        st.session_state[chosen_key] = None

    if items_key not in st.session_state:
        start()

    items = st.session_state[items_key]
    q_idx = st.session_state[idx_key]

    if q_idx < len(items):
        item = items[q_idx]
        st.write(f"Pregunta **{q_idx + 1}** de **{len(items)}**  ·  Aciertos: **{st.session_state[score_key]}**")
        st.markdown(f"**{item['q']}**")

        if not st.session_state[answered_key]:
            for opt in item["options"]:
                if st.button(opt, key=f"{key_prefix}-{q_idx}-{opt}", use_container_width=True):
                    st.session_state[answered_key] = True
                    st.session_state[chosen_key] = opt
                    if opt == item["correct"]:
                        st.session_state[score_key] += 1
                    st.rerun()
        else:
            for opt in item["options"]:
                if opt == item["correct"]:
                    st.success(opt)
                elif opt == st.session_state[chosen_key]:
                    st.error(opt)
                else:
                    st.write(opt)

            if st.button("Siguiente ➡️", key=f"{key_prefix}-next-{q_idx}", use_container_width=True):
                st.session_state[idx_key] += 1
                st.session_state[answered_key] = False
                st.session_state[chosen_key] = None
                st.rerun()
    else:
        pct = st.session_state[score_key] / len(items)
        st.subheader(f"Resultado: {st.session_state[score_key]} de {len(items)} correctas")
        if pct == 1:
            st.balloons()
            st.write(mastery_msg)
        elif pct >= 0.6:
            st.write(good_msg)
        else:
            st.write(low_msg)

        if st.button("🔁 Reintentar", key=f"{key_prefix}-retry", use_container_width=True):
            start()
            st.rerun()


# ============================================================
# CONSTRUCTORES DE CADA QUIZ
# ============================================================
def build_quiz_rapido():
    rule_indices = random.sample(range(len(RULES)), 6)
    rule_questions = []
    for i in rule_indices:
        wrong_pool = [r["title"] for j, r in enumerate(RULES) if j != i]
        wrongs = random.sample(wrong_pool, 3)
        rule_questions.append({"q": RULES[i]["quiz_text"], "correct": RULES[i]["title"], "wrongs": wrongs})
    items = rule_questions + EXTRA_QUESTIONS
    random.shuffle(items)
    for item in items:
        options = item["wrongs"] + [item["correct"]]
        random.shuffle(options)
        item["options"] = options
    return items


def build_fill_blank():
    items = []
    for fb in FILL_BLANKS:
        options = fb["options"][:]
        random.shuffle(options)
        items.append({"q": fb["sentence"], "correct": fb["answer"], "options": options})
    random.shuffle(items)
    return items


def build_caso_dia():
    items = []
    for case in CASES:
        wrong_pool = [r["title"] for r in RULES if r["title"] != case["rule"]]
        wrongs = random.sample(wrong_pool, 3)
        options = wrongs + [case["rule"]]
        random.shuffle(options)
        items.append({"q": case["scenario"], "correct": case["rule"], "options": options})
    random.shuffle(items)
    return items


def build_mv_tf():
    items = []
    for s in MV_STATEMENTS:
        items.append({
            "q": s["text"],
            "correct": "Verdadero" if s["is_true"] else "Falso",
            "options": ["Verdadero", "Falso"],
        })
    random.shuffle(items)
    return items


# ============================================================
# TABS
# ============================================================
tab_cards, tab_mv, tab_fill, tab_order, tab_case, tab_quiz, tab_mvquiz = st.tabs(
    ["📇 Tarjetas", "🎯 Misión y visión", "🧩 Completa la frase", "🔢 Ordena las 11",
     "💼 Caso del día", "🧠 Quiz rápido", "✅ Quiz V/F Misión y Visión"]
)

# ----------------------------
# TAB: Tarjetas (flashcards)
# ----------------------------
with tab_cards:
    if "card_idx" not in st.session_state:
        st.session_state.card_idx = 0
    if "flipped" not in st.session_state:
        st.session_state.flipped = False

    idx = st.session_state.card_idx
    rule = RULES[idx]

    st.write(f"Regla **{idx + 1}** de **{len(RULES)}**")

    if st.session_state.flipped:
        st.markdown(f'<div class="card"><p>{idx + 1}. {rule["text"]}</p></div>', unsafe_allow_html=True)
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
# TAB: Misión y visión
# ----------------------------
with tab_mv:
    st.markdown(f'<div class="mv-card"><h4>🎯 Misión</h4><p>{MISSION}</p></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="mv-card"><h4>🔭 Visión</h4><p>{VISION}</p></div>', unsafe_allow_html=True)

# ----------------------------
# TAB: Completa la frase
# ----------------------------
with tab_fill:
    st.caption("Elige la palabra o frase que falta en cada regla del código.")
    run_mcq(
        "fill",
        build_fill_blank,
        mastery_msg="¡Perfecto! Te sabes el código al pie de la letra.",
        good_msg="Buen trabajo, repasa las tarjetas de las que fallaste.",
        low_msg="Vale la pena repasar las tarjetas antes de reintentar este modo.",
    )

# ----------------------------
# TAB: Ordena las 11
# ----------------------------
with tab_order:
    st.caption("Selecciona las reglas en el orden en que aparecen en el Código de Honor (de la 1 a la 11).")

    def reset_order():
        titles = [r["title"] for r in RULES]
        shuffled = titles[:]
        random.shuffle(shuffled)
        st.session_state.order_remaining = shuffled
        st.session_state.order_chosen = []
        st.session_state.order_checked = False

    if "order_remaining" not in st.session_state:
        reset_order()

    if not st.session_state.order_checked:
        st.write(f"Seleccionadas: **{len(st.session_state.order_chosen)}** de **{len(RULES)}**")

        if st.session_state.order_chosen:
            st.markdown("**Tu orden hasta ahora:**")
            st.write(" → ".join(f"{i + 1}. {t}" for i, t in enumerate(st.session_state.order_chosen)))

        cols = st.columns(2)
        for i, title in enumerate(st.session_state.order_remaining):
            col = cols[i % 2]
            with col:
                if st.button(title, key=f"order-btn-{title}", use_container_width=True):
                    st.session_state.order_chosen.append(title)
                    st.session_state.order_remaining.remove(title)
                    st.rerun()

        if len(st.session_state.order_remaining) == 0:
            if st.button("✅ Verificar orden", use_container_width=True, key="order-check"):
                st.session_state.order_checked = True
                st.rerun()
    else:
        correct_titles = [r["title"] for r in RULES]
        chosen = st.session_state.order_chosen
        correct_count = sum(1 for i, t in enumerate(chosen) if t == correct_titles[i])
        st.subheader(f"Resultado: {correct_count} de {len(RULES)} en la posición correcta")
        for i, t in enumerate(chosen):
            if t == correct_titles[i]:
                st.success(f"{i + 1}. {t}")
            else:
                st.error(f"{i + 1}. {t}  →  debía ser: {correct_titles[i]}")
        if correct_count == len(RULES):
            st.balloons()

    if st.button("🔁 Reiniciar", use_container_width=True, key="order-reset"):
        reset_order()
        st.rerun()

# ----------------------------
# TAB: Caso del día
# ----------------------------
with tab_case:
    st.caption("Un mini escenario real: elige qué regla del código aplica.")
    run_mcq(
        "case",
        build_caso_dia,
        mastery_msg="¡Excelente criterio! Sabes aplicar el código en la práctica.",
        good_msg="Buen trabajo, repasa los casos en los que dudaste.",
        low_msg="Vale la pena repasar las tarjetas y volver a intentar los casos.",
    )

# ----------------------------
# TAB: Quiz rápido
# ----------------------------
with tab_quiz:
    run_mcq(
        "quiz",
        build_quiz_rapido,
        mastery_msg="Excelente, dominas el código, la misión y la visión.",
        good_msg="Buen trabajo, repasa lo que fallaste en la sección de tarjetas.",
        low_msg="Vale la pena repasar las tarjetas de nuevo antes de reintentar.",
    )

# ----------------------------
# TAB: Quiz V/F Misión y Visión
# ----------------------------
with tab_mvquiz:
    st.caption("Verdadero o falso: ¿de verdad interiorizaste la misión y la visión?")
    run_mcq(
        "mvquiz",
        build_mv_tf,
        mastery_msg="¡Perfecto! Tienes muy clara la misión y la visión.",
        good_msg="Buen trabajo, repasa la pestaña de Misión y visión.",
        low_msg="Vale la pena releer la Misión y la Visión antes de reintentar.",
    )
