
import streamlit as st


def show_preview(df):
    st.subheader("📄 Dataset Preview")

    rows = st.selectbox(
        "Rows to Display",
        [5, 10, 25, 50],
        index=1,
        key="preview_rows"
    )

    st.dataframe(
        df.head(rows),
        use_container_width=True,
        hide_index=True
    )

    st.divider()
