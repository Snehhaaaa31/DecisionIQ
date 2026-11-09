
import streamlit as st
import hashlib

from utils.loader import load_dataset
from utils.metrics import get_metrics, show_metrics
from utils.preview import show_preview
from utils.summary import show_summary
from utils.explorer import show_column_explorer
from utils.missing import show_missing_analysis
from utils.statistics import show_statistics
from utils.ai_snapshot import show_ai_snapshot
from utils.download import download_dataset


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
        file_bytes = uploaded_file.getvalue()

        # Identify whether this is a new dataset
        file_hash = hashlib.md5(file_bytes).hexdigest()

        if st.session_state.get("uploaded_file_hash") != file_hash:

            with st.spinner("Loading dataset..."):
                df = load_dataset(uploaded_file)

                st.session_state["df"] = df
                st.session_state["uploaded_file_hash"] = file_hash
                st.session_state["metrics"] = get_metrics(df)
                st.session_state.pop("ai_snapshot_generated", None)

        # Retrieve saved dataset and metrics
        df = st.session_state["df"]
        metrics = st.session_state["metrics"]

        st.success("✅ Dataset uploaded successfully!")

        show_metrics(metrics)
        show_preview(df)
        show_summary(uploaded_file, metrics)
        show_column_explorer(df)
        show_missing_analysis(df)
        show_statistics(df)

        # Generate AI snapshot only when requested
        st.subheader("🤖 AI Dataset Snapshot")

        if st.button("Generate AI Snapshot"):
            with st.spinner("Generating AI insights..."):
                show_ai_snapshot(df, metrics)

        download_dataset(df)

    except Exception as e:
        st.error(f"Dataset processing failed: {e}")
