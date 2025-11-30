import streamlit as st
import numpy as np

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Q-SmartGrid Neon Simulation",
    layout="wide"
)

# =========================
# NEON CYBERGRID CSS
# =========================
NEON_CSS = """
<style>
body {
    background: radial-gradient(circle at top, #051622 0%, #000814 60%, #000000 100%) !important;
    font-family: 'Segoe UI', sans-serif;
    color: #e0faff;
}

#MainMenu, header, footer {visibility: hidden;}

.neon-title {
    color: #5efcff;
    font-size: 2.7rem;
    text-align: center;
    font-weight: 900;
    text-shadow: 0 0 10px #00d9ff, 0 0 25px #00a3cc;
    margin-bottom: 0.3rem;
}

.neon-subtitle {
    font-size: 1rem;
    color: #9ae6ff;
    text-align: center;
    opacity: 0.9;
    margin-bottom: 2rem;
}

/* Input + Panels */
.neon-panel {
    border-radius: 18px;
    padding: 1.2rem;
    background: linear-gradient(135deg, rgba(3,31,43,0.95), rgba(0,79,102,0.92));
    border: 1px solid rgba(0,255,255,0.45);
    box-shadow: 0 0 20px rgba(0,255,255,0.2), 0 0 45px rgba(0,145,165,0.35);
}

.neon-header-small {
    font-size: 0.85rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #5efcff;
    margin-bottom: 0.4rem;
}

.neon-label {
    color: #e0faff;
    font-size: 0.9rem;
    font-weight: 500;
}

/* Optimize Button */
.neon-button > button {
    width: 100%;
    border-radius: 999px !important;
    border: 1px solid rgba(0,255,234,0.8) !important;
    background: linear-gradient(135deg, #17c964, #00664f) !important;
    color: #eaffff !important;
    font-weight: 800 !important;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    box-shadow: 0 0 18px rgba(0,255,153,0.9), 0 0 40px rgba(0,255,234,0.6);
}

.neon-button > button:hover {
    filter: brightness(1.2);
}

/* IMPACT METRICS */
.impact-box {
    margin-top: 1rem;
    padding: 1.3rem;
    border-radius: 18px;
    border: 1px solid rgba(0,255,255,0.45);
    background: linear-gradient(135deg, rgba(0,34,43,0.95), rgba(0,79,102,0.92));
    box-shadow: 0 0 20px rgba(0,255,255,0.2), 0 0 45px rgba(0,145,165,0.35);
}

.impact-title {
    color: #5efcff;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    margin-bottom: 1rem;
    text-transform: uppercase;
}

/* metric card */
.metric {
    padding: 1rem 1.2rem;
    border-radius: 14px;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, rgba(1,63,73,1), rgba(0,122,153,0.8));
    border: 1px solid rgba(0,255,234,0.35);
    box-shadow: 0 0 16px rgba(0,255,255,0.3);
}

.metric-value {
    font-size: 1.8rem;
    font-weight: 800;
    color: #67ffcc;
    text-shadow: 0 0 12px rgba(0,255,153,0.8);
}

.metric-label {
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #d5faf6;
}
</style>
"""
st.markdown(NEON_CSS, unsafe_allow_html=True)

# =========================
# TITLE SECTION
# =========================
st.markdown('<div class="neon-title">Q-SmartGrid Control Room</div>', unsafe_allow_html=True)
st.markdown('<div class="neon-subtitle">Adjust building loads, then let AI + Quantum Optimization reduce waste automatically ⚡</div>', unsafe_allow_html=True)

# =========================
# INPUT PANEL
# =========================
left_col, right_col = st.columns([1.2, 1.4])

with left_col:
    st.markdown('<div class="neon-panel">', unsafe_allow_html=True)
    st.markdown('<div class="neon-header-small">INPUT • BUILDING LOADS</div>', unsafe_allow_html=True)
    st.markdown('<p class="neon-label">Set the current consumption for each building (kW):</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1: A = st.slider("🏢 A", 10, 120, 60)
    with c2: B = st.slider("🏭 B", 10, 120, 80)
    with c3: C = st.slider("🏨 C", 10, 120, 45)

    original_loads = np.array([A, B, C])
    total_before = original_loads.sum()
    peak_before = int(original_loads.max())

    st.caption(f"🔋 Total load before optimization: **{total_before} kW**")
    st.markdown("</div>", unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="neon-panel">', unsafe_allow_html=True)
    st.markdown('<div class="neon-header-small">CURRENT GRID STATE • BEFORE OPTIMIZATION</div>', unsafe_allow_html=True)
    before_data = {"Buildings": ["A", "B", "C"], "Load (kW)": original_loads}
    st.bar_chart(before_data, x="Buildings", y="Load (kW)", use_container_width=True)
    st.caption(f"⚠️ Peak load before: **{peak_before} kW**")
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.markdown('<div class="neon-button">', unsafe_allow_html=True)
optimize_clicked = st.button("🚀 Optimize with Q-SmartGrid")
st.markdown("</div>", unsafe_allow_html=True)
st.write("")

# =========================
# OPTIMIZATION LOGIC
# =========================
if optimize_clicked:

    optimized = np.maximum(10, original_loads - np.random.randint(8, 25, size=3))
    total_after = optimized.sum()
    peak_after = int(optimized.max())

    savings = total_before - total_after
    peak_reduction = peak_before - peak_after
    savings_percent = round((savings / total_before) * 100, 2)

    col_before, col_after, col_metrics = st.columns([1.1, 1.1, 0.8])

    with col_before:
        st.markdown('<div class="neon-panel">', unsafe_allow_html=True)
        st.markdown('<div class="neon-header-small">GRID SNAPSHOT • BEFORE</div>', unsafe_allow_html=True)
        st.bar_chart({"Buildings": ["A", "B", "C"], "Load (kW)": original_loads})
        st.caption("🔸 Unoptimized state – higher peak & waste.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_after:
        st.markdown('<div class="neon-panel">', unsafe_allow_html=True)
        st.markdown('<div class="neon-header-small">OPTIMIZED GRID • AFTER Q-SMARTGRID</div>', unsafe_allow_html=True)
        st.bar_chart({"Buildings": ["A", "B", "C"], "Load (kW)": optimized})
        st.caption("✅ Optimized distribution – lower peak & total load.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_metrics:
        st.markdown('<div class="impact-box">', unsafe_allow_html=True)
        st.markdown('<div class="impact-title">⚡ IMPACT METRICS</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="metric"><div class="metric-value">{int(savings)} kW</div><div class="metric-label">TOTAL SAVINGS</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric"><div class="metric-value">{int(peak_reduction)} kW</div><div class="metric-label">PEAK REDUCTION</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric"><div class="metric-value">{savings_percent}%</div><div class="metric-label">EFFICIENCY GAIN</div></div>', unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.caption("👆 اضبطي الأحمال، ثم اضغطي **Optimize** لتشاهدي تأثير Q-SmartGrid.")
