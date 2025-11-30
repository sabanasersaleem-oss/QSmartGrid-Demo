import streamlit as st
import numpy as np

# =========================
# 🔧 Page Config
# =========================
st.set_page_config(
    page_title="Q-SmartGrid Neon Simulation",
    layout="wide"
)

# =========================
# 🎨 Custom CSS – Neon Cyber Grid Style
# =========================
NEON_CSS = """
<style>
body {
    background: radial-gradient(circle at top, #051622 0%, #000814 60%, #000 100%) !important;
    font-family: 'Segoe UI', sans-serif;
    color: #e0faff;
}

/* remove streamlit crap */
#MainMenu, header, footer {visibility: hidden;}

.neon-title {
    color: #5efcff;
    font-size: 2.8rem;
    text-align: center;
    font-weight: 900;
    text-shadow: 0 0 8px #00d9ff, 0 0 22px #00a3cc;
    margin-bottom: 0.3rem;
}

.neon-subtitle {
    font-size: 1rem;
    color: #9ae6ff;
    text-align: center;
    opacity: 0.9;
    margin-bottom: 2rem;
}

/* IMPACT PANEL */
.impact-box {
    margin-top: 1rem;
    padding: 1.3rem;
    border-radius: 18px;
    border: 1px solid rgba(0,255,255,0.45);
    background: linear-gradient(135deg, rgba(0,34,43,0.95), rgba(0,79,102,0.92));
    box-shadow: 0 0 20px rgba(0,255,255,0.2), 0 0 45px rgba(0,145,165,0.35);
}

/* METRIC title */
.impact-title {
    color: #5efcff;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    margin-bottom: 1rem;
    text-transform: uppercase;
}

/* Metric card */
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
# 🧠 Title Section
# =========================
st.markdown('<div class="neon-title">Q-SmartGrid Control Room</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="neon-subtitle">Adjust building loads, then let AI + Quantum Optimization reduce waste automatically ⚡</div>',
    unsafe_allow_html=True
)

# =========================
# 🔌 Input Panel – Building Loads
# =========================
left_col, right_col = st.columns([1.2, 1.4])
with col_metrics:
    st.markdown('<div class="impact-box">', unsafe_allow_html=True)
    st.markdown('<div class="impact-title">⚡ IMPACT METRICS</div>', unsafe_allow_html=True)

    st.markdown(
        f'''
        <div class="metric">
            <div class="metric-value">{int(savings)} kW</div>
            <div class="metric-label">TOTAL SAVINGS</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown(
        f'''
        <div class="metric">
            <div class="metric-value">{int(peak_reduction)} kW</div>
            <div class="metric-label">PEAK REDUCTION</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown(
        f'''
        <div class="metric">
            <div class="metric-value">{savings_percent}%</div>
            <div class="metric-label">EFFICIENCY GAIN</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================
# 📊 Before Optimization Chart
# =========================
with right_col:
    st.markdown('<div class="neon-panel">', unsafe_allow_html=True)
    st.markdown('<div class="neon-header-small">CURRENT GRID STATE • BEFORE OPTIMIZATION</div>', unsafe_allow_html=True)

    # Wrap labels & chart
    before_chart_data = {
        "Buildings": ["A", "B", "C"],
        "Load (kW)": original_loads
    }
    st.bar_chart(before_chart_data, x="Buildings", y="Load (kW)", use_container_width=True)

    peak_before = int(original_loads.max())
    st.caption(f"⚠️ Peak building load: **{peak_before} kW**")

    st.markdown("</div>", unsafe_allow_html=True)

st.write("")  # spacer

# =========================
# 🚀 Optimize Button
# =========================
st.markdown('<div class="neon-button">', unsafe_allow_html=True)
optimize_clicked = st.button("🚀 Optimize with Q-SmartGrid")
st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# =========================
# 🧮 Optimization Logic & Results
# =========================
if optimize_clicked:
    col_before, col_after, col_metrics = st.columns([1.1, 1.1, 0.8])

    with col_before:
        st.markdown('<div class="neon-panel">', unsafe_allow_html=True)
        st.markdown('<div class="neon-header-small">GRID SNAPSHOT • BEFORE</div>', unsafe_allow_html=True)

        before_data = {
            "Buildings": ["A", "B", "C"],
            "Load (kW)": original_loads
        }
        st.bar_chart(before_data, x="Buildings", y="Load (kW)", use_container_width=True)

        st.caption("🔸 Unoptimized state – higher peak & more waste.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_after:
        st.markdown('<div class="neon-panel">', unsafe_allow_html=True)
        st.markdown('<div class="neon-header-small">OPTIMIZED GRID • AFTER Q-SMARTGRID</div>', unsafe_allow_html=True)

        # Simple quantum-inspired effect: reduce loads but keep minimum 10
        optimized = np.maximum(10, original_loads - np.random.randint(8, 25, size=3))
        total_after = optimized.sum()
        peak_after = int(optimized.max())

        after_data = {
            "Buildings": ["A", "B", "C"],
            "Load (kW)": optimized
        }
        st.bar_chart(after_data, x="Buildings", y="Load (kW)", use_container_width=True)

        st.caption("✅ Optimized distribution – lower peak & lower total load.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_metrics:
        st.markdown('<div class="neon-panel">', unsafe_allow_html=True)
        st.markdown('<div class="neon-header-small">IMPACT METRICS</div>', unsafe_allow_html=True)

        savings = total_before - total_after
        savings_percent = round((savings / total_before) * 100, 2) if total_before > 0 else 0
        peak_reduction = peak_before - peak_after

        st.markdown(
            f'''
            <div class="neon-metric">
                <span class="label">Total Savings</span>
                <span class="value">{int(savings)} kW</span>
            </div>
            ''',
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div class="neon-metric">
                <span class="label">Peak Reduction</span>
                <span class="value">{int(peak_reduction)} kW</span>
            </div>
            ''',
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div class="neon-metric">
                <span class="label">Efficiency Gain</span>
                <span class="value">{savings_percent}%</span>
            </div>
            ''',
            unsafe_allow_html=True
        )

        st.markdown(
            '<p style="font-size:0.8rem;color:#9ca3af;">Each optimization run simulates how AI + Quantum redistribute loads to minimize waste.</p>',
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.caption("👆  **Optimize** .")
