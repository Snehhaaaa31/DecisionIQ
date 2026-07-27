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

    col1, col2 = st.columns(2)

    with col1:

        st.metric("Data Type", str(data.dtype))
        st.metric("Missing Values", int(data.isnull().sum()))
        st.metric("Unique Values", int(data.nunique()))

    with col2:

        if pd.api.types.is_numeric_dtype(data):

            st.metric("Minimum", round(data.min(), 2))
            st.metric("Maximum", round(data.max(), 2))
            st.metric("Average", round(data.mean(), 2))

        else:

            mode = data.mode()

            if len(mode) > 0:
                st.metric("Most Frequent", str(mode.iloc[0]))
            else:
                st.metric("Most Frequent", "-")

            st.metric("Unique Categories", data.nunique())

    st.write("### Sample Values")

    st.dataframe(
        data.dropna().head(10),
        use_container_width=True,
        hide_index=True
    )

    st.divider()