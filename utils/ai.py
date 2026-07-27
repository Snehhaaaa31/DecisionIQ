import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def build_business_context(df):
    """Create a business summary from the uploaded dataframe."""

    context = []

    context.append(f"Dataset contains {len(df):,} records.")
    context.append(f"Columns: {', '.join(df.columns)}")

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols):
        context.append("\nNumeric Summary:\n")
        context.append(df[numeric_cols].describe().to_string())

    # Common business metrics
    if "Sales" in df.columns:
        context.append(f"\nTotal Sales: ₹{df['Sales'].sum():,.2f}")

    if "Profit" in df.columns:
        context.append(f"Total Profit: ₹{df['Profit'].sum():,.2f}")

    if "Quantity" in df.columns:
        context.append(f"Total Quantity Sold: {df['Quantity'].sum():,.0f}")

    if "Category" in df.columns:
        context.append(
            "\nTop Categories:\n"
            + df.groupby("Category")["Sales"].sum().sort_values(ascending=False).to_string()
            if "Sales" in df.columns
            else "\nCategory Counts:\n"
            + df["Category"].value_counts().to_string()
        )

    if "Region" in df.columns and "Sales" in df.columns:
        context.append(
            "\nRegional Sales:\n"
            + df.groupby("Region")["Sales"].sum().sort_values(ascending=False).to_string()
        )

    return "\n".join(context)


def ask_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content


def generate_business_report(context):

    prompt = f"""
You are a Senior Business Intelligence Consultant.

Using ONLY the business information below, create a professional report.

{context}

Report Sections:

1. Executive Summary

2. KPI Highlights

3. Business Performance

4. Risks & Concerns

5. Opportunities

6. Strategic Recommendations

Use markdown.
Do not invent numbers.
"""

    return ask_ai(prompt)


def generate_recommendations(context):

    prompt = f"""
You are a Strategy Consultant.

Business Information:

{context}

Give practical recommendations for:

- Revenue Growth
- Profit Improvement
- Customer Strategy
- Inventory
- Operations
- Pricing
- Top 5 Priority Actions

Use bullet points.
"""

    return ask_ai(prompt)


def chat_with_data(question, context):

    prompt = f"""
You are DecisionIQ.

You are an AI Business Intelligence Assistant.

Business Information:

{context}

Question:

{question}

Rules:

- Answer only using the information above.
- Never invent statistics.
- Be concise.
- End with one actionable recommendation whenever possible.
"""

    return ask_ai(prompt)