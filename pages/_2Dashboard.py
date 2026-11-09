
import streamlit as st

from utils.dashboard import (
    apply_filters,
    show_kpis,
    line_chart,
    bar_chart,
    pie_chart,
    correlation,
    top_records
)

st.title("📊 Business Dashboard")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

# Retrieve the stored dataset
df = st.session_state["df"]

# Apply dashboard filters
filtered_df = apply_filters(df)

if filtered_df.empty:
    st.warning("No records found for the selected filters.")
    st.stop()

# Display KPIs
show_kpis(filtered_df)

# Charts
c1, c2 = st.columns(2)

with c1:
    line_chart(filtered_df)

with c2:
    bar_chart(filtered_df)

c1, c2 = st.columns(2)

with c1:
    pie_chart(filtered_df)

with c2:
    correlation(filtered_df)

# Top records
top_records(filtered_df)
