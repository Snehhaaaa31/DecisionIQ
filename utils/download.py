import streamlit as st


def download_dataset(df):

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Clean Dataset",
        data=csv,
        file_name="clean_dataset.csv",
        mime="text/csv",
        use_container_width=True
    )