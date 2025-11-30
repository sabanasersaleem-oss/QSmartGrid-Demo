import streamlit as st
import numpy as np
import random

st.set_page_config(page_title="Q-SmartGrid Simulation", layout="wide")

st.title("⚡ Q-SmartGrid – Live Energy Optimization Simulation")
st.write("تحكم بأحمال المباني ثم اضغط Optimize لتشاهد كيف يقلل النظام الهدر 🔋✨")

# -----------------------------
# Step 1: User Inputs (Build Load)
# -----------------------------
st.subheader("🔧 اختر استهلاك المباني (kW)")

col1, col2, col3 = st.columns(3)

with col1:
    A = st.slider("Building A", 10, 100, 50)

with col2:
    B = st.slider("Building B", 10, 100, 70)

with col3:
    C = st.slider("Building C", 10, 100, 40)

original_loads = np.array([A, B, C])
total_before = original_loads.sum()

st.write("### 🔋 قبل التحسين:")
st.bar_chart(original_loads)

# -----------------------------
# Step 2: Optimization Button
# -----------------------------
if st.button("🚀 Optimize with Q-SmartGrid"):

    st.subheader("⚛️ Quantum Optimization Running…")
    st.write("جارٍ حساب أفضل توزيع للطاقة باستخدام Quantum-Inspired Optimization…")

    # Fake but realistic quantum optimization
    optimized = np.maximum(10, original_loads - np.random.randint(5, 25, size=3))

    total_after = optimized.sum()

    # Metrics
    savings = total_before - total_after
    savings_percent = round((savings / total_before) * 100, 2)

    peak_reduction = round((max(original_loads) - max(optimized)), 2)

    # -----------------------------
    # Step 3: Show Results
    # -----------------------------
    st.success("✨ Optimization Complete!")

    st.write("### 🔋 بعد التحسين:")
    st.bar_chart(optimized)

    st.metric("📉 الوفر الكلي (kW)", f"{savings} kW")
    st.metric("⚡ تقليل الضغط على الذروة (kW)", peak_reduction)
    st.metric("💰 نسبة التوفير (%)", f"{savings_percent}%")

    st.info("💡 Q-SmartGrid يقلل الهدر ويعيد توزيع الطاقة تلقائياً لتحقيق أعلى كفاءة.")
