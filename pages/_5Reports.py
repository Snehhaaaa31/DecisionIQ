import streamlit as st

from utils.ai import (
    build_business_context,
    generate_business_report,
    generate_recommendations,
)

from utils.report import generate_report


st.set_page_config(page_title="DecisionIQ Report", page_icon="📄")

st.title("📄 DecisionIQ Business Report")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

st.markdown(
    """
Generate a complete AI-powered executive business report summarizing
your dataset, business performance, and strategic recommendations.
"""
)

# -------------------------
# Dataset Overview
# -------------------------

st.subheader("📊 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

rows, cols = df.shape

with col1:
    st.metric("Rows", f"{rows:,}")

with col2:
    st.metric("Columns", cols)

with col3:
    st.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

with col4:
    st.metric(
        "Numeric Columns",
        len(df.select_dtypes(include="number").columns)
    )

st.divider()

# -------------------------
# Generate Report
# -------------------------

if st.button(
    "🚀 Generate AI Business Report",
    use_container_width=True,
):

    with st.spinner("Analyzing dataset..."):

        context = build_business_context(df)

        business_report = generate_business_report(context)

        recommendations = generate_recommendations(context)

        forecast_summary = ""

        if "forecast_summary" in st.session_state:
            forecast_summary = st.session_state["forecast_summary"]

        report = generate_report(
            df=df,
            business_report=business_report,
            recommendations=recommendations,
            forecast_summary=forecast_summary,
        )

    st.success("Report Generated Successfully!")

    st.divider()

    st.markdown(report)

    st.download_button(
        label="⬇ Download Report (.md)",
        data=report,
        file_name="DecisionIQ_Report.md",
        mime="text/markdown",
        use_container_width=True,
    )