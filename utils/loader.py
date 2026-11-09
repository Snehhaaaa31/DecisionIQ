
import pandas as pd
import streamlit as st
from io import BytesIO


@st.cache_data(show_spinner=False)
def _load_dataset_cached(file_bytes, filename):

    if filename.lower().endswith(".csv"):
        return pd.read_csv(BytesIO(file_bytes))

    elif filename.lower().endswith(".xlsx"):
        return pd.read_excel(BytesIO(file_bytes))

    else:
        raise ValueError("Unsupported file format.")


def load_dataset(uploaded_file):

    file_bytes = uploaded_file.getvalue()

    return _load_dataset_cached(
        file_bytes,
        uploaded_file.name
    )
