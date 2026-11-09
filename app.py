
import streamlit as st
from pathlib import Path

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="DecisionIQ",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# LOAD CUSTOM CSS
# =====================================================

css_path = Path("styles/style.css")

if css_path.exists():
    st.html(f"<style>{css_path.read_text(encoding='utf-8')}</style>")


# =====================================================
# HOME PAGE
# =====================================================

def home():

    # HERO SECTION
    st.html("""
    <div class="hero-container">

        <div class="hero-tag">
            ✦ NEXT-GENERATION BUSINESS INTELLIGENCE
        </div>

        <h1 class="hero-title">
            Turn Your Data Into
            <span>Smarter Decisions.</span>
        </h1>

        <p class="hero-description">
            Welcome to DecisionIQ — an AI-powered business intelligence
            platform that transforms raw business data into actionable
            insights through advanced analytics, predictive forecasting,
            anomaly detection and intelligent recommendations.
        </p>

        <div class="hero-highlights">
            <span>✦ Data Analytics</span>
            <span>✦ Predictive Intelligence</span>
            <span>✦ AI-Powered Insights</span>
        </div>

    </div>
    """)

    # GET STARTED BUTTON
    st.markdown('<div class="start-button">', unsafe_allow_html=True)

    if st.button("🚀 Let's Get Started", use_container_width=True):
        st.switch_page(upload_page)

    st.markdown("</div>", unsafe_allow_html=True)

    # WHY DECISIONIQ
    st.html("""
    <div class="section-heading">
        <h2>✨ Why DecisionIQ?</h2>
        <p>
            Everything you need to transform business data
            into meaningful decisions.
        </p>
    </div>
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.html("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>Smart Analytics</h3>
            <p>
                Explore your business data through interactive
                dashboards, KPIs and visual reports.
            </p>
        </div>
        """)

    with col2:
        st.html("""
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <h3>Predictive Forecasting</h3>
            <p>
                Identify future trends and forecast business
                performance using machine learning.
            </p>
        </div>
        """)

    with col3:
        st.html("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3>AI-Powered Insights</h3>
            <p>
                Discover patterns, detect anomalies and generate
                intelligent business recommendations.
            </p>
        </div>
        """)

    # WORKFLOW SECTION
    st.html("""
    <div class="workflow-section">
        <div class="section-eyebrow">HOW IT WORKS</div>
        <h2>Your Data. Your Insights. Better Decisions.</h2>
        <p>
            Move from raw data to actionable intelligence
            in a few simple steps.
        </p>
    </div>
    """)

    w1, w2, w3, w4 = st.columns(4)

    workflow = [
        ("01", "Upload", "Import your business dataset."),
        ("02", "Analyze", "Explore KPIs and visualizations."),
        ("03", "Predict", "Forecast trends and performance."),
        ("04", "Decide", "Use AI insights to make decisions.")
    ]

    for col, (number, title, description) in zip(
        [w1, w2, w3, w4], workflow
    ):
        with col:
            st.html(f"""
            <div class="workflow-card">
                <div class="workflow-number">{number}</div>
                <h4>{title}</h4>
                <p>{description}</p>
            </div>
            """)

    # FOOTER
    st.html("""
    <div class="footer">
        DecisionIQ © 2026 · Intelligent Business Decisions
    </div>
    """)


# =====================================================
# REGISTER ALL EXISTING PAGES
# =====================================================

home_page = st.Page(
    home,
    title="Home",
    icon="🏠",
    default=True
)

upload_page = st.Page(
    "pages/_1Upload_Dataset.py.py",
    title="Upload Dataset",
    icon="📂"
)

dashboard_page = st.Page(
    "pages/_2Dashboard.py",
    title="Dashboard",
    icon="📊"
)

forecast_page = st.Page(
    "pages/_3Forecasting.py",
    title="Forecasting",
    icon="📈"
)

insights_page = st.Page(
    "pages/_4AI_Insights.py",
    title="AI Insights",
    icon="🤖"
)

reports_page = st.Page(
    "pages/_5Reports.py",
    title="Reports",
    icon="📄"
)


# =====================================================
# CENTRAL NAVIGATION
# =====================================================

current_page = st.navigation(
    [
        home_page,
        upload_page,
        dashboard_page,
        forecast_page,
        insights_page,
        reports_page
    ],
    position="hidden"
)


# =====================================================
# CUSTOM SHARED SIDEBAR
# =====================================================

with st.sidebar:

    st.html("""
    <div class="sidebar-brand">
        <div class="brand-icon">📊</div>

        <div>
            <div class="brand-text">DecisionIQ</div>
            <div class="brand-subtitle">
                INTELLIGENCE PLATFORM
            </div>
        </div>
    </div>

    <div class="sidebar-heading">
        WORKSPACE
    </div>
    """)

    st.page_link(
        home_page,
        label="Home",
        icon="🏠"
    )

    st.page_link(
        upload_page,
        label="Upload Dataset",
        icon="📂"
    )

    st.page_link(
        dashboard_page,
        label="Dashboard",
        icon="📊"
    )

    st.page_link(
        forecast_page,
        label="Forecasting",
        icon="📈"
    )

    st.page_link(
        insights_page,
        label="AI Insights",
        icon="🤖"
    )

    st.page_link(
        reports_page,
        label="Reports",
        icon="📄"
    )

    st.html("""
    <div class="sidebar-status">
        <div class="status-line">
            <span class="status-dot"></span>
            System Operational
        </div>

        <div class="status-version">
            DecisionIQ | Version 2.0
        </div>
    </div>
    """)


# =====================================================
# DISPLAY SELECTED PAGE
# =====================================================

current_page.run()
