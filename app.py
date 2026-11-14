"""
app.py — Production Streamlit UI for the Plant Disease Diagnostic System.

Run with:
    streamlit run app.py

Features
--------
• Drag-and-drop or file-browse image upload (JPG / PNG / WEBP)
• Real-time CNN inference with top-5 predictions
• Interactive confidence bar chart (Plotly)
• Detailed disease info card: symptoms, causes, treatment, prevention
• Healthy / Diseased visual feedback with colour-coded badges
• Sidebar with model metadata and supported-crops reference
• Fully responsive single-page layout
"""

from __future__ import annotations

import time
from pathlib import Path

import streamlit as st
from PIL import Image
import plotly.graph_objects as go

# ── Local imports ──────────────────────────────────────────────────────────
from model import load_model
from utils import predict, is_healthy, confidence_color, confidence_label
from disease_info import get_disease_info

# ── Page configuration ─────────────────────────────────────────────────────
st.set_page_config(
    page_title="🌿 Plant Disease Detector",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* ---- Global ---- */
    .block-container { padding-top: 1.5rem; }

    /* ---- Hero badge ---- */
    .hero-badge {
        display: inline-block;
        padding: 0.35em 0.8em;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.95rem;
        margin-bottom: 0.3rem;
    }
    .badge-healthy  { background: #d4edda; color: #155724; }
    .badge-diseased { background: #f8d7da; color: #721c24; }

    /* ---- Confidence pill ---- */
    .conf-pill {
        display: inline-block;
        padding: 0.25em 0.75em;
        border-radius: 20px;
        font-weight: 600;
        font-size: 1.05rem;
        color: #fff;
    }

    /* ---- Info cards ---- */
    .info-card {
        background: #f8f9fa;
        border-left: 4px solid #28a745;
        border-radius: 4px;
        padding: 1em 1.2em;
        margin: 0.5em 0;
    }
    .info-card.disease {
        border-left-color: #dc3545;
    }

    /* ---- Sidebar metric ---- */
    .sidebar-metric {
        background: #262730;
        border-radius: 8px;
        padding: 0.8em 1em;
        margin-bottom: 0.5em;
        text-align: center;
    }
    .sidebar-metric h4 { margin: 0; color: #fafafa; font-size: 0.85rem; }
    .sidebar-metric p  { margin: 0; color: #2ecc71; font-size: 1.4rem; font-weight: 700; }
</style>
""", unsafe_allow_html=True)


# ── Load model (cached) ───────────────────────────────────────────────────
@st.cache_resource(show_spinner="Loading CNN model …")
def _load():
    return load_model()

model, class_names, device = _load()


# ── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image(
        "https://img.icons8.com/fluency/96/leaf.png",
        width=64,
    )
    st.title("🌿 Plant Disease Detector")
    st.caption("Powered by a custom 4-block CNN trained on the New Plant Diseases Dataset.")

    st.divider()

    st.subheader("📊 Model Info")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(
            '<div class="sidebar-metric"><h4>Accuracy</h4><p>97.48 %</p></div>',
            unsafe_allow_html=True,
        )
    with col_b:
        st.markdown(
            '<div class="sidebar-metric"><h4>Classes</h4><p>38</p></div>',
            unsafe_allow_html=True,
        )

    st.markdown(f"**Device:** `{device}`")
    st.markdown("**Architecture:** Custom CNN (4 Conv + 3 FC)")
    st.markdown("**Input size:** 128 × 128 px")
    st.markdown("**Dataset:** New Plant Diseases Dataset")

    st.divider()

    # Supported plants
    plants = sorted({cn.split("___")[0].replace("_", " ") for cn in class_names})
    st.subheader("🌱 Supported Crops")
    st.write(", ".join(plants))

    st.divider()
    st.caption("© 2026 Plant Disease Diagnostic System  \nBuilt with Streamlit + PyTorch")


# ── Main Area ──────────────────────────────────────────────────────────────
st.markdown("## 🔬 Upload a Leaf Image for Diagnosis")
st.markdown(
    "Take a clear photo of a **single leaf** and upload it below. "
    "The model will predict the disease (or confirm the plant is healthy) "
    "along with confidence scores and actionable advice."
)

uploaded = st.file_uploader(
    "Choose a leaf image …",
    type=["jpg", "jpeg", "png", "webp"],
    help="Supported formats: JPG, PNG, WEBP.  Best results with a clear, well-lit, single-leaf photo.",
)

if uploaded is not None:
    image = Image.open(uploaded)

    # ── Layout: image + results side by side ───────────────────────────
    col_img, col_res = st.columns([1, 1.3], gap="large")

    with col_img:
        st.image(image, caption="Uploaded leaf image", use_container_width=True)

    with col_res:
        with st.spinner("Running inference …"):
            start = time.perf_counter()
            results = predict(image, model, class_names, device, top_k=5)
            elapsed = time.perf_counter() - start

        top = results[0]
        healthy = is_healthy(top["class_name"])

        # ── Headline result ────────────────────────────────────────────
        badge_cls = "badge-healthy" if healthy else "badge-diseased"
        badge_txt = "✅ Healthy" if healthy else "⚠️ Disease Detected"
        st.markdown(f'<span class="hero-badge {badge_cls}">{badge_txt}</span>', unsafe_allow_html=True)

        st.markdown(f"### {top['display_name']}")

        conf_col = confidence_color(top["probability"])
        st.markdown(
            f'<span class="conf-pill" style="background:{conf_col}">'
            f'{top["probability"]*100:.1f} % — {confidence_label(top["probability"])}'
            f'</span>',
            unsafe_allow_html=True,
        )
        st.caption(f"Inference time: **{elapsed*1000:.0f} ms** on `{device}`")

    st.divider()

    # ── Top-5 interactive bar chart ────────────────────────────────────
    st.subheader("📊 Top-5 Prediction Probabilities")

    labels = [r["display_name"] for r in results][::-1]
    probs  = [r["probability"] * 100 for r in results][::-1]
    colours = [confidence_color(r["probability"]) for r in results][::-1]

    fig = go.Figure(go.Bar(
        x=probs,
        y=labels,
        orientation="h",
        marker_color=colours,
        text=[f"{p:.1f} %" for p in probs],
        textposition="outside",
        hovertemplate="%{y}<br>Confidence: %{x:.2f} %<extra></extra>",
    ))
    fig.update_layout(
        xaxis_title="Confidence (%)",
        xaxis_range=[0, max(probs) * 1.18],
        yaxis_title="",
        height=300,
        margin=dict(l=10, r=30, t=10, b=40),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(size=13),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ── Disease detail card ────────────────────────────────────────────
    info = get_disease_info(top["class_name"])
    card_cls = "info-card" if healthy else "info-card disease"

    st.subheader(f"{'🌿' if healthy else '🦠'} Detailed Information")

    tab_symptoms, tab_treatment, tab_prevention = st.tabs(
        ["🩺 Symptoms", "💊 Treatment", "🛡️ Prevention"]
    )

    with tab_symptoms:
        st.markdown(f"**Identified condition:** {info['disease']}")
        st.markdown(f"**Plant:** {info['plant']}")
        st.markdown(f"**Cause:** {info['causes']}")
        for s in info["symptoms"]:
            st.markdown(f"- {s}")

    with tab_treatment:
        if healthy:
            st.success("No treatment is required — your plant looks healthy! 🎉")
        for t in info["treatment"]:
            st.markdown(f"✔️ {t}")

    with tab_prevention:
        for p in info["prevention"]:
            st.markdown(f"🔹 {p}")

    # ── Full top-5 table ───────────────────────────────────────────────
    with st.expander("📋 Full Top-5 Results Table", expanded=False):
        table_data = []
        for i, r in enumerate(results, 1):
            table_data.append({
                "Rank": i,
                "Prediction": r["display_name"],
                "Plant": r["plant"],
                "Condition": r["condition"],
                "Confidence (%)": f"{r['probability']*100:.2f}",
            })
        st.table(table_data)

else:
    # ── Placeholder when no image is uploaded ──────────────────────────
    st.info("👆 Upload a leaf image above to get started.", icon="🌿")

    # Show some example class names
    st.markdown("---")
    st.markdown("### 🗂️ Diseases Recognized by this Model")

    diseases = [cn for cn in class_names if "healthy" not in cn.lower()]
    healthy_classes = [cn for cn in class_names if "healthy" in cn.lower()]

    col_d, col_h = st.columns(2)
    with col_d:
        st.markdown(f"**🦠 Diseases ({len(diseases)})**")
        for d in diseases:
            parts = d.split("___")
            plant = parts[0].replace("_", " ")
            cond = parts[1].replace("_", " ").title() if len(parts) > 1 else ""
            st.markdown(f"- **{plant}** — {cond}")
    with col_h:
        st.markdown(f"**🌿 Healthy Classes ({len(healthy_classes)})**")
        for h in healthy_classes:
            plant = h.split("___")[0].replace("_", " ")
            st.markdown(f"- ✅ {plant}")

