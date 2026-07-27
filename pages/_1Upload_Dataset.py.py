import streamlit as st

from utils.loader import load_dataset
from utils.metrics import get_metrics, show_metrics
from utils.preview import show_preview
from utils.summary import show_summary
from utils.explorer import show_column_explorer
from utils.missing import show_missing_analysis
from utils.statistics import show_statistics
from utils.ai_snapshot import show_ai_snapshot
from utils.download import download_dataset


st.set_page_config(
    page_title="Upload Dataset",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Upload Dataset")

st.caption(
    "Upload your CSV or Excel dataset to begin AI-powered business analysis."
)

uploaded_file = st.file_uploader(
    "Choose your dataset",
    type=["csv", "xlsx"]
)

if uploaded_file:

    try:

        df = load_dataset(uploaded_file)

        st.session_state["df"] = df

        metrics = get_metrics(df)

        st.success("✅ Dataset uploaded successfully!")

        show_metrics(metrics)

        show_preview(df)

        show_summary(uploaded_file, metrics)

        show_column_explorer(df)

        show_missing_analysis(df)

        show_statistics(df)

        show_ai_snapshot(df, metrics)

        download_dataset(df)

    except Exception as e:
        st.exception(e)