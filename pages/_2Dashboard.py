import streamlit as st

from utils.dashboard import *

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Business Dashboard")

if "df" not in st.session_state:

    st.warning("Please upload a dataset first.")

    st.stop()

df=st.session_state["df"]

df=apply_filters(df)

show_kpis(df)

c1,c2=st.columns(2)

with c1:
    line_chart(df)

with c2:
    bar_chart(df)

c1,c2=st.columns(2)

with c1:
    pie_chart(df)

with c2:
    correlation(df)

top_records(df)