import streamlit as st
import pandas as pd


def show_summary(uploaded_file, metrics):

    st.subheader("📋 Dataset Summary")

    summary = pd.DataFrame(
        {
            "Metric": [
                "File Name",
                "Rows",
                "Columns",
                "Numeric Columns",
                "Categorical Columns",
                "Missing Values",
                "Duplicate Rows",
                "Memory Usage (MB)"
            ],

            "Value": [
                uploaded_file.name,
                metrics["rows"],
                metrics["columns"],
                metrics["numeric"],
                metrics["categorical"],
                metrics["missing"],
                metrics["duplicates"],
                metrics["memory"]
            ]
        }
    )

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    st.divider()