import streamlit as st


def show_ai_snapshot(df, metrics):

    st.subheader("🤖 AI Dataset Snapshot")

    score = 100

    if metrics["missing"] > 0:
        score -= 20

    if metrics["duplicates"] > 0:
        score -= 10

    if metrics["numeric"] == 0:
        score -= 30

    if score >= 90:
        quality = "🟢 Excellent"
    elif score >= 70:
        quality = "🟡 Good"
    else:
        quality = "🔴 Needs Cleaning"

    st.info(f"""
### Dataset Health Score : **{score}/100**

**Overall Quality:** {quality}

✅ Rows : {metrics["rows"]:,}

✅ Columns : {metrics["columns"]}

🔢 Numeric Columns : {metrics["numeric"]}

📝 Categorical Columns : {metrics["categorical"]}

⚠ Missing Values : {metrics["missing"]}

🔁 Duplicate Rows : {metrics["duplicates"]}

📦 Memory Usage : {metrics["memory"]} MB
""")

    st.success("🚀 Dataset is ready for Dashboard Analysis.")

    st.divider()