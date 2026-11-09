
import streamlit as st
import pandas as pd

from utils.forecasting import (
    run_forecast,
    show_forecast,
    show_components,
    show_table,
    download_forecast
)


st.title("📈 Sales Forecasting")

# Check uploaded dataset
if "df" not in st.session_state:
    st.warning("Upload a dataset first.")
    st.stop()

df = st.session_state["df"]

# Identify date columns
date_cols = []

for col in df.columns:

    if pd.api.types.is_datetime64_any_dtype(df[col]):
        date_cols.append(col)

    elif col.lower() in [
        "date", "order_date", "order date", "ds"
    ]:
        date_cols.append(col)

# Identify numeric columns
numeric_cols = df.select_dtypes(
    include="number"
).columns.tolist()

if not date_cols:
    st.error("No valid date column found.")
    st.stop()

if not numeric_cols:
    st.error("No numeric columns found.")
    st.stop()

# Column selection
date_col = st.selectbox(
    "Select Date Column",
    date_cols
)

target_col = st.selectbox(
    "Select Target Column",
    numeric_cols
)

# Forecast period
periods = st.slider(
    "Forecast Months",
    min_value=1,
    max_value=24,
    value=12
)

# Generate forecast
if st.button("🚀 Generate Forecast", use_container_width=True):

    try:

        with st.spinner("Generating Forecast..."):

            model, prophet_df, forecast = run_forecast(
                df,
                date_col,
                target_col,
                periods
            )

        st.success("Forecast generated successfully!")

        st.subheader("Forecast Visualization")
        show_forecast(prophet_df, forecast)

        show_components(model, forecast)

        show_table(forecast)

        download_forecast(forecast)

    except Exception as e:

        st.error(f"Forecasting failed: {e}")
