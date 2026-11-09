
import streamlit as st


# =====================================================
# STATISTICAL SUMMARY
# =====================================================

@st.cache_data(show_spinner=False)
def calculate_statistics(df):

    return df.describe(
        include="all"
    ).T


# =====================================================
# DISPLAY STATISTICS
# =====================================================

def show_statistics(df):

    st.subheader("📊 Statistical Summary")

    with st.expander(
        "View Complete Statistics",
        expanded=False
    ):

        with st.spinner("Calculating statistics..."):

            stats = calculate_statistics(df)

        st.dataframe(
            stats,
            use_container_width=True
        )

    st.divider()
