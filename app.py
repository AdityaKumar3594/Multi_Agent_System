import streamlit as st

st.set_page_config(
    page_title="Multi-Agent Research",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

:root {
    --glass-bg:     rgba(255,255,255,0.07);
    --glass-border: rgba(255,255,255,0.18);
    --glass-shadow: rgba(0,0,0,0.4);
    --accent-1:     #00f5d4;
    --accent-2:     #7b5ea7;
    --accent-3:     #f72585;
    --text-primary: #e8eaf6;
    --text-muted:   rgba(232,234,246,0.55);
}

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main {
    background: linear-gradient(135deg,#0d0221 0%,#1a0533 30%,#0a1628 65%,#051020 100%) !important;
    font-family:'Outfit',sans-serif;
    color: var(--text-primary);
}

/* animated orbs */
[data-testid="stAppViewContainer"]::before,
[data-testid="stAppViewContainer"]::after {
    content:'';position:fixed;border-radius:50%;filter:blur(90px);
    z-index:0;pointer-events:none;
    animation:drift 14s ease-in-out infinite alternate;
}
[data-testid="stAppViewContainer"]::before {
    width:560px;height:560px;top:-140px;left:-120px;
    background:radial-gradient(circle,rgba(123,94,167,.38) 0%,transparent 70%);
}
[data-testid="stAppViewContainer"]::after {
    width:440px;height:440px;bottom:-100px;right:-100px;animation-delay:-7s;
    background:radial-gradient(circle,rgba(0,245,212,.25) 0%,transparent 70%);
}
@keyframes drift{0%{transform:translate(0,0) scale(1)}100%{transform:translate(40px,30px) scale(1.09)}}

#MainMenu,footer,header,[data-testid="stToolbar"]{display:none !important}

.block-container{max-width:1020px !important;padding:2rem 2rem !important;position:relative;z-index:1}

/* ── hero ── */
.hero{text-align:center;padding:3rem 1rem 2rem}
.hero-badge{
    display:inline-block;font-family:'Space Mono',monospace;font-size:.7rem;
    letter-spacing:.22em;text-transform:uppercase;color:var(--accent-1);
    background:rgba(0,245,212,.1);border:1px solid rgba(0,245,212,.3);
    border-radius:100px;padding:.35rem 1.1rem;margin-bottom:1.3rem;
}
.hero h1{
    font-size:clamp(2rem,5vw,3.2rem);font-weight:700;line-height:1.15;margin:0 0 1rem;
    background:linear-gradient(135deg,#fff 20%,var(--accent-1) 60%,var(--accent-2) 100%);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.hero p{color:var(--text-muted);font-size:1rem;font-weight:300;max-width:540px;margin:0 auto;line-height:1.75}

/* ── glass card ── */
.glass-card{
    background:var(--glass-bg);
    backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);
    border:1px solid var(--glass-border);border-radius:20px;
    padding:1.8rem 2rem;box-shadow:0 8px 32px var(--glass-shadow);
    margin-bottom:1.4rem;position:relative;overflow:hidden;
}
.glass-card::before{
    content:'';position:absolute;top:0;left:0;right:0;height:1px;
    background:linear-gradient(90deg,transparent,rgba(255,255,255,.22),transparent);
}

/* ── stepper (pure HTML, single markdown block) ── */
.stepper-wrap{display:flex;justify-content:center;align-items:flex-start;gap:0;margin:1.6rem 0 2.2rem;width:100%}
.s-item{display:flex;flex-direction:column;align-items:center;flex:1;position:relative}
.s-item:not(:last-child)::after{
    content:'';position:absolute;top:23px;left:calc(50% + 26px);right:calc(-50% + 26px);
    height:1px;background:var(--glass-border);z-index:0;
}
.s-dot{
    width:48px;height:48px;border-radius:50%;
    background:rgba(255,255,255,.05);border:1.5px solid var(--glass-border);
    display:flex;align-items:center;justify-content:center;
    font-size:1.2rem;position:relative;z-index:1;
}
.s-dot.active{border-color:var(--accent-1);box-shadow:0 0 22px rgba(0,245,212,.5);animation:pulse-ring 1.8s ease-in-out infinite}
.s-dot.done{border-color:var(--accent-1);background:rgba(0,245,212,.15);color:var(--accent-1);font-size:.95rem;font-weight:700}
@keyframes pulse-ring{0%,100%{box-shadow:0 0 16px rgba(0,245,212,.4)}50%{box-shadow:0 0 30px rgba(0,245,212,.75)}}
.s-label{margin-top:.5rem;font-size:.72rem;font-weight:500;letter-spacing:.05em;color:var(--text-muted);text-align:center}
.s-label.active{color:var(--accent-1)}
.s-label.done{color:rgba(0,245,212,.7)}

/* ── result cards ── */
.result-header{display:flex;align-items:center;gap:.7rem;margin-bottom:.9rem}
.r-icon{
    width:36px;height:36px;border-radius:10px;
    display:flex;align-items:center;justify-content:center;font-size:1rem;flex-shrink:0;
}
.r-icon.search{background:rgba(0,245,212,.12);border:1px solid rgba(0,245,212,.28)}
.r-icon.reader{background:rgba(247,37,133,.12);border:1px solid rgba(247,37,133,.28)}
.r-icon.writer{background:rgba(123,94,167,.18);border:1px solid rgba(123,94,167,.32)}
.r-icon.critic{background:rgba(255,183,3,.12);border:1px solid rgba(255,183,3,.28)}
.r-title{font-size:.75rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--text-muted)}
.r-content{
    background:rgba(0,0,0,.22);border:1px solid rgba(255,255,255,.07);border-radius:12px;
    padding:1.1rem 1.3rem;font-size:.9rem;line-height:1.75;color:var(--text-primary);
    white-space:pre-wrap;max-height:300px;overflow-y:auto;
    scrollbar-width:thin;scrollbar-color:rgba(0,245,212,.3) transparent;
}

/* ── input overrides ── */
[data-testid="stTextInput"] input{
    background:rgba(255,255,255,.06) !important;
    border:1px solid var(--glass-border) !important;
    border-radius:14px !important;color:var(--text-primary) !important;
    font-family:'Outfit',sans-serif !important;font-size:1rem !important;
    padding:.8rem 1.2rem !important;
}
[data-testid="stTextInput"] input:focus{
    border-color:var(--accent-1) !important;
    box-shadow:0 0 0 3px rgba(0,245,212,.15) !important;outline:none !important;
}
[data-testid="stTextInput"] label{
    color:var(--text-muted) !important;font-size:.82rem !important;
    font-weight:500 !important;letter-spacing:.06em !important;
}

/* ── button ── */
.stButton > button{
    width:100%;
    background:linear-gradient(135deg,rgba(0,245,212,.18),rgba(123,94,167,.28)) !important;
    border:1px solid rgba(0,245,212,.45) !important;border-radius:14px !important;
    color:#fff !important;font-family:'Outfit',sans-serif !important;
    font-size:.97rem !important;font-weight:600 !important;letter-spacing:.04em !important;
    padding:.8rem 2rem !important;cursor:pointer !important;
    transition:all .3s ease !important;backdrop-filter:blur(8px) !important;
}
.stButton > button:hover{
    background:linear-gradient(135deg,rgba(0,245,212,.28),rgba(123,94,167,.42)) !important;
    box-shadow:0 0 28px rgba(0,245,212,.3) !important;
    transform:translateY(-2px) !important;border-color:var(--accent-1) !important;
}
.stButton > button:active{transform:translateY(0) !important}

/* download button */
[data-testid="stDownloadButton"] button{
    background:linear-gradient(135deg,rgba(123,94,167,.25),rgba(0,245,212,.15)) !important;
    border:1px solid rgba(123,94,167,.45) !important;border-radius:14px !important;
    color:#fff !important;font-family:'Outfit',sans-serif !important;
    font-size:.95rem !important;font-weight:600 !important;
    padding:.8rem 2rem !important;width:100%;
    transition:all .3s ease !important;
}
[data-testid="stDownloadButton"] button:hover{
    box-shadow:0 0 24px rgba(123,94,167,.4) !important;
    transform:translateY(-2px) !important;
}

/* progress bar */
[data-testid="stProgress"] > div > div{
    background:linear-gradient(90deg,var(--accent-1),var(--accent-2)) !important;
    border-radius:100px !important;
}
[data-testid="stProgress"]{background:rgba(255,255,255,.07) !important;border-radius:100px !important}

/* status/info/success/error */
[data-testid="stInfo"]{background:rgba(0,245,212,.08) !important;border:1px solid rgba(0,245,212,.2) !important;border-radius:12px !important}
[data-testid="stSuccess"]{background:rgba(0,245,212,.1) !important;border:1px solid rgba(0,245,212,.35) !important;border-radius:12px !important}
[data-testid="stError"]{background:rgba(247,37,133,.1) !important;border:1px solid rgba(247,37,133,.3) !important;border-radius:12px !important}

hr{border:none;border-top:1px solid var(--glass-border);margin:1.8rem 0}
</style>
""", unsafe_allow_html=True)


# ── Stepper helper (pure self-contained HTML) ─────────────────────────────────
STEPS = [
    ("🔍", "Search"),
    ("📖", "Reader"),
    ("✍️", "Writer"),
    ("🧠", "Critic"),
]

def stepper_html(active: int) -> str:
    """Return a self-contained stepper HTML string. active=-1 means idle."""
    items = ""
    for i, (icon, label) in enumerate(STEPS):
        if i < active:
            dot_cls, lbl_cls, disp = "done", "done", "✓"
        elif i == active:
            dot_cls, lbl_cls, disp = "active", "active", icon
        else:
            dot_cls, lbl_cls, disp = "", "", icon
        items += (
            f'<div class="s-item">'
            f'  <div class="s-dot {dot_cls}">{disp}</div>'
            f'  <div class="s-label {lbl_cls}">{label}</div>'
            f'</div>'
        )
    return f'<div class="stepper-wrap">{items}</div>'


def normalize_body(body):
    if isinstance(body, list):
        return "\n".join(str(item) for item in body)
    if isinstance(body, dict):
        import json
        return json.dumps(body, indent=2)
    return str(body)


def result_card(icon: str, cls: str, title: str, body: str):
    text_body = normalize_body(body)
    safe_body = text_body.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    st.markdown(
        f'<div class="glass-card">'
        f'  <div class="result-header">'
        f'    <div class="r-icon {cls}">{icon}</div>'
        f'    <span class="r-title">{title}</span>'
        f'  </div>'
        f'  <div class="r-content">{safe_body}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">⬡ Multi-Agent System</div>
  <h1>Research Intelligence<br>Pipeline</h1>
  <p>A four-stage AI swarm that searches, scrapes, writes,<br>and critiques — so you don't have to.</p>
</div>
""", unsafe_allow_html=True)

# ── INPUT ROW ─────────────────────────────────────────────────────────────────

col_in, col_btn = st.columns([4, 1.2], gap="medium")
with col_in:
    topic = st.text_input(
        "RESEARCH TOPIC",
        placeholder="e.g. Quantum computing breakthroughs in 2025 …",
        key="topic_input",
    )
with col_btn:
    st.markdown("<br>", unsafe_allow_html=True)
    run_btn = st.button("🚀  Run Pipeline", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)   # close glass-card

# ── IDLE STATE ────────────────────────────────────────────────────────────────
if not run_btn:
    st.markdown(stepper_html(-1), unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align:center;color:rgba(232,234,246,.3);"
        "font-size:.88rem;margin-top:.4rem;font-style:italic;'>"
        "Enter a topic and hit "
        "<strong style='color:rgba(0,245,212,.65)'>Run Pipeline</strong> to begin."
        "</div>",
        unsafe_allow_html=True,
    )

# ── PIPELINE RUN ──────────────────────────────────────────────────────────────
else:
    if not topic.strip():
        st.error("Please enter a research topic before running the pipeline.")
        st.stop()

    stepper_ph  = st.empty()
    progress_ph = st.empty()
    status_ph   = st.empty()

    def set_step(n: int, msg: str):
        stepper_ph.markdown(stepper_html(n), unsafe_allow_html=True)
        progress_ph.progress(n / len(STEPS))
        status_ph.info(f"**{msg}**")

    state = {}

    with st.status("🔄  Running multi-agent pipeline …", expanded=True) as status_box:
        try:
            from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

            # Step 1 – Search
            st.write("**Step 1 / 4** — Search Agent gathering information …")
            set_step(0, "Search Agent is working …")
            search_result = build_search_agent().invoke({
                "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
            })
            state["search_results"] = search_result["messages"][-1].content
            st.write("✅  Search complete.")

            # Step 2 – Reader
            st.write("**Step 2 / 4** — Reader Agent scraping top resources …")
            set_step(1, "Reader Agent is scraping …")
            reader_result = build_reader_agent().invoke({
                "messages": [("user",
                    f"Based on the following search results about '{topic}', "
                    f"pick the most relevant URL and scrape it for deeper content.\n\n"
                    f"Search Results:\n{state['search_results'][:800]}"
                )]
            })
            state["scraped_content"] = reader_result["messages"][-1].content
            st.write("✅  Scraping complete.")

            # Step 3 – Writer
            st.write("**Step 3 / 4** — Writer Chain drafting the report …")
            set_step(2, "Writer is drafting …")
            state["report"] = writer_chain.invoke({
                "topic": topic,
                "research": (
                    f"SEARCH RESULTS:\n{state['search_results']}\n\n"
                    f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
                ),
            })
            st.write("✅  Report drafted.")

            # Step 4 – Critic
            st.write("**Step 4 / 4** — Critic reviewing the report …")
            set_step(3, "Critic is reviewing …")
            state["feedback"] = critic_chain.invoke({"report": state["report"]})
            st.write("✅  Review complete.")

            status_box.update(label="✅  Pipeline complete!", state="complete", expanded=False)

        except Exception as e:
            status_box.update(label="❌  Pipeline failed", state="error", expanded=True)
            st.error(f"Error: {e}")
            st.stop()

    # All done – final stepper state
    stepper_ph.markdown(stepper_html(len(STEPS)), unsafe_allow_html=True)
    progress_ph.progress(1.0)
    status_ph.success("🎉 Research pipeline finished successfully!")

    # ── Results ───────────────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown(
        "<div style='text-align:center;font-family:\"Space Mono\",monospace;"
        "font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;"
        "color:rgba(232,234,246,.4);margin-bottom:1.6rem;'>Pipeline Output</div>",
        unsafe_allow_html=True,
    )

    c_left, c_right = st.columns(2, gap="large")
    with c_left:
        result_card("🔍", "search", "Search Results",  state.get("search_results", "—"))
        result_card("✍️", "writer", "Written Report",  state.get("report", "—"))
    with c_right:
        result_card("📖", "reader", "Scraped Content", state.get("scraped_content", "—"))
        result_card("🧠", "critic", "Critic Feedback",  state.get("feedback", "—"))

    # ── Download ──────────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        full_md = (
            f"# Research Report: {topic}\n\n"
            f"## Search Results\n{state.get('search_results','')}\n\n"
            f"## Scraped Content\n{state.get('scraped_content','')}\n\n"
            f"## Written Report\n{state.get('report','')}\n\n"
            f"## Critic Feedback\n{state.get('feedback','')}"
        )
        st.download_button(
            label="⬇  Download Full Report",
            data=full_md,
            file_name=f"research_{topic[:40].replace(' ','_')}.md",
            mime="text/markdown",
            use_container_width=True,
        )