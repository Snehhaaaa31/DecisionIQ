import streamlit as st


def get_metrics(df):

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing": df.isnull().sum().sum(),
        "duplicates": df.duplicated().sum(),
        "numeric": len(df.select_dtypes(include="number").columns),
        "categorical": len(
            df.select_dtypes(
                include=["object", "category", "string"]
            ).columns
        ),
        "memory": round(
            df.memory_usage(deep=True).sum() / 1024**2,
            2
        ),
    }


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
        metrics["missing"]
    )

    c4.metric(
        "🔁 Duplicates",
        metrics["duplicates"]
    )

    st.divider()