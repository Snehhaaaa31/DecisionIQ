
import streamlit as st
import pandas as pd


def show_column_explorer(df):
    st.subheader("🔍 Column Explorer")

    column = st.selectbox(
        "Select a Column",
        df.columns,
        key="column_explorer"
    )

    data = df[column]

    # Calculate common statistics once
    missing_count = int(data.isna().sum())
    unique_count = int(data.nunique())

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Data Type", str(data.dtype))
        st.metric("Missing Values", missing_count)
        st.metric("Unique Values", unique_count)

    with col2:
        if pd.api.types.is_numeric_dtype(data):
            valid_data = data.dropna()

            if not valid_data.empty:
                st.metric("Minimum", round(valid_data.min(), 2))
                st.metric("Maximum", round(valid_data.max(), 2))
                st.metric("Average", round(valid_data.mean(), 2))
            else:
                st.metric("Minimum", "-")
                st.metric("Maximum", "-")
                st.metric("Average", "-")

        else:
            mode = data.mode(dropna=True)

            most_frequent = (
                str(mode.iloc[0]) if not mode.empty else "-"
            )

            st.metric("Most Frequent", most_frequent)
            st.metric("Unique Categories", unique_count)

    st.write("### Sample Values")

    st.dataframe(
        data.dropna().head(10).to_frame(),
        use_container_width=True,
        hide_index=True
    )

    st.divider()
