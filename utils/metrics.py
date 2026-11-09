
import streamlit as st


# =====================================================
# DATASET METRICS
# =====================================================

@st.cache_data(show_spinner=False)
def get_metrics(df):

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns

    categorical_cols = df.select_dtypes(
        include=["object", "category", "string"]
    ).columns

    return {
        "rows": len(df),

        "columns": len(df.columns),

        "missing": int(df.isnull().sum().sum()),

        "duplicates": int(df.duplicated().sum()),

        "numeric": len(numeric_cols),

        "categorical": len(categorical_cols),

        "memory": round(
            df.memory_usage(deep=True).sum() / 1024**2,
            2
        ),
    }


# =====================================================
# DISPLAY DATASET HEALTH
# =====================================================

def show_metrics(metrics):

    st.subheader("📊 Dataset Health")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📄 Rows",
        f"{metrics['rows']:,}"
    )

    c2.metric(
        "🧾 Columns",
        metrics["columns"]
    )

    c3.metric(
        "⚠ Missing",
        f"{metrics['missing']:,}"
    )

    c4.metric(
        "🔁 Duplicates",
        f"{metrics['duplicates']:,}"
    )

    st.divider()
