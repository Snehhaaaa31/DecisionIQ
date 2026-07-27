import streamlit as st


def show_statistics(df):

    st.subheader("📊 Statistical Summary")

    with st.expander("View Complete Statistics", expanded=False):

        st.dataframe(
            df.describe(include="all").T,
            use_container_width=True
        )

    st.divider()