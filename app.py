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
    background: radial-gradient(circle at top, #0f172a 0, #020617 45%, #000 100%) !important;
    color: #e5e7eb !important;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

section.main > div {
    padding-top: 1rem;
}

/* Hide the default Streamlit menu & footer */
#MainMenu, footer, header {visibility: hidden;}

.neon-title {
    font-size: 2.6rem;
    font-weight: 800;
    text-align: center;
    letter-spacing: 0.08em;
    color: #22d3ee;
    text-shadow: 0 0 8px rgba(34,211,238,0.8),
                 0 0 20px rgba(56,189,248,0.7);
    margin-bottom: 0.2rem;
}

.neon-subtitle {
    text-align: center;
    color: #a5b4fc;
    font-size: 0.98rem;
    margin-bottom: 1.5rem;
}

.neon-panel {
    border-radius: 18px;
    padding: 1.1rem 1.3rem;
    background: linear-gradient(135deg, rgba(15,23,42,0.95), rgba(8,47,73,0.95));
    border: 1px solid rgba(56,189,248,0.5);
    box-shadow:
       0 0 16px rgba(56,189,248,0.4),
       0 0 40px rgba(8,47,73,0.6);
}

.neon-header-small {
    font-size: 0.9rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #38bdf8;
    margin-bottom: 0.2rem;
}

.neon-label {
    font-weight: 600;
    font-size: 0.9rem;
    color: #e5e7eb;
}

.neon-metric {
    background: radial-gradient(circle at top left, rgba(34,197,94,0.17), rgba(15,23,42,0.9));
    border-radius: 14px;
    padding: 0.8rem 1rem;
    border: 1px solid rgba(34,197,94,0.6);
    margin-bottom: 0.6rem;
}

.neon-metric span.label {
    display: block;
    font-size: 0.75rem;
    color: #bbf7d0;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.neon-metric span.value {
    display: block;
    font-size: 1.2rem;
    font-weight: 700;
    color: #bbf7d0;
}

.neon-button > button {
    width: 100%;
    border-radius: 999px !important;
    border: 1px solid rgba(45,212,191,0.9) !important;
    background: radial-gradient(circle at top, #22c55e, #0f766e) !important;
    color: #ecfeff !important;
    font-weight: 700 !important;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    box-shadow:
       0 0 14px rgba(16,185,129,0.9),
       0 0 40px rgba(45,212,191,0.8);
}

.neon-button > button:hover {
    filter: brightness(1.1);
    box-shadow:
       0 0 20px rgba(16,185,129,1),
       0 0 50px rgba(45,212,191,1);
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

with left_col:
    st.markdown('<div class="neon-panel">', unsafe_allow_html=True)
    st.markdown('<div class="neon-header-small">INPUT • BUILDING LOADS</div>', unsafe_allow_html=True)
    st.markdown('<p class="neon-label">Set the current consumption for each building (kW):</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        A = st.slider("🏢 A", 10, 120, 60)
    with c2:
        B = st.slider("🏭 B", 10, 120, 80)
    with c3:
        C = st.slider("🏨 C", 10, 120, 45)

    original_loads = np.array([A, B, C])
    total_before = original_loads.sum()

    st.write("")
    st.caption("🔋 Total load before optimization: **{} kW**".format(int(total_before)))

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
    st.caption("👆 اضبطي الأحمال للمباني، ثم اضغطي زر **Optimize** لترين تأثير Q-SmartGrid لايف أمام اللجنة.")
