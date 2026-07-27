import streamlit as st
import pandas as pd


def show_missing_analysis(df):

    st.subheader("⚠️ Missing Value Analysis")

    missing = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum().values,
        "Missing %": (
            df.isnull().sum() / len(df) * 100
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

    if missing["Missing Values"].sum() == 0:

        st.success("🎉 No missing values found.")

    else:

        st.warning(
            f"Found {missing['Missing Values'].sum()} missing values."
        )

    st.divider()