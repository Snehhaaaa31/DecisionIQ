import streamlit as st

from utils.forecasting import *

st.set_page_config(
    page_title="Forecasting",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Sales Forecasting")

if "df" not in st.session_state:

    st.warning("Upload a dataset first.")

    st.stop()

df = st.session_state["df"]

date_cols = df.select_dtypes(
    include=["datetime", "object"]
).columns

numeric_cols = df.select_dtypes(
    include="number"
).columns

date_col = st.selectbox(
    "Select Date Column",
    date_cols
)

target_col = st.selectbox(
    "Select Target Column",
    numeric_cols
)

periods = st.slider(
    "Forecast Months",
    1,
    24,
    12
)

if st.button("Generate Forecast"):

    with st.spinner("Generating Forecast..."):

        model, prophet_df, forecast = run_forecast(
            df,
            date_col,
            target_col,
            periods
        )

        show_forecast(
            prophet_df,
            forecast
        )

        show_components(
            model,
            forecast
        )

        show_table(
            forecast
        )

        download_forecast(
            forecast
        )