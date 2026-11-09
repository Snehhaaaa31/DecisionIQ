
import streamlit as st
import pandas as pd


def show_missing_analysis(df):
    st.subheader("⚠️ Missing Value Analysis")

    # Calculate missing values once
    missing_counts = df.isna().sum()
    total_missing = int(missing_counts.sum())

    missing = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": missing_counts.values,
        "Missing %": (
            missing_counts / max(len(df), 1) * 100
        ).round(2)
    })

    missing = missing.sort_values(
        "Missing Values",
        ascending=False
    )

    st.dataframe(
        missing,
        use_container_width=True,
        hide_index=True
    )

    if total_missing == 0:
        st.success("🎉 No missing values found.")
    else:
        st.warning(f"Found {total_missing} missing values.")

    st.divider()
