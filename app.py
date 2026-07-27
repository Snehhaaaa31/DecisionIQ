import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="DecisionIQ",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# LOAD CSS
# =====================================

def load_css():
    with open("styles/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("📊 DecisionIQ")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    (
        "🏠 Home",
        "📂 Upload Dataset",
        "📊 Dashboard",
        "📈 Forecasting",
        "🤖 AI Advisor",
        "💬 AI Chat",
        "📄 Reports"
    )
)

st.sidebar.markdown("---")
st.sidebar.success("Version 1.0")

# =====================================
# HOME PAGE
# =====================================

if page == "🏠 Home":

    st.markdown(
    """
    <div class="hero">
        <h1>📊 DecisionIQ</h1>
        <h2>AI-Powered Business Intelligence Platform</h2>
        <p>
            Transform raw business data into intelligent business decisions
            using AI-powered analytics, forecasting, anomaly detection,
            dashboards and strategic recommendations.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
    st.write("")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.button(
            "🚀 Get Started",
            use_container_width=True
        )

    st.write("")
    st.write("")

    st.markdown("## ✨ Why DecisionIQ?")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="feature-card">
            <h3>📂 Upload Dataset</h3>
            <p>
            Upload CSV or Excel datasets instantly and
            begin analysis in seconds.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="feature-card">
            <h3>📊 Interactive Dashboard</h3>
            <p>
            Beautiful KPI cards,
            charts and business insights.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="feature-card">
            <h3>📈 Forecasting</h3>
            <p>
            Predict future sales,
            revenue and business trends.
            </p>
        </div>
        """, unsafe_allow_html=True)

    c5, c6 = st.columns(2)

    with c5:
        st.markdown("""
        <div class="feature-card">
            <h3>🤖 AI Advisor</h3>
            <p>
            Receive intelligent
            business recommendations.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c6:
        st.markdown("""
        <div class="feature-card">
            <h3>💬 AI Chat</h3>
            <p>
            Chat with your uploaded
            business dataset.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.success(
        "🚀 Ready to explore your business data? Upload your dataset to get started."
    )

