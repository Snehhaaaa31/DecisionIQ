import streamlit as st

from utils.ai import (
    build_business_context,
    generate_business_report,
    generate_recommendations,
    chat_with_data,
)

st.title("🤖 AI Insights")

if "df" not in st.session_state:
    st.warning("Upload a dataset first.")
    st.stop()

df = st.session_state["df"]

context = build_business_context(df)

tab1, tab2 = st.tabs(["📊 AI Insights", "💬 Chat"])

with tab1:

    st.subheader("Business Report")

    if st.button("Generate Business Report"):

        with st.spinner("Generating report..."):
            report = generate_business_report(context)

        st.markdown(report)

    st.divider()

    st.subheader("Recommendations")

    if st.button("Generate Recommendations"):

        with st.spinner("Thinking..."):
            recommendations = generate_recommendations(context)

        st.markdown(recommendations)

with tab2:

    st.subheader("Chat with DecisionIQ")

    question = st.text_input(
        "Ask a business question",
        placeholder="Example: Which category is most profitable?"
    )

    if st.button("Ask AI"):

        if question.strip():

            with st.spinner("Analyzing..."):

                answer = chat_with_data(question, context)

            st.markdown(answer)