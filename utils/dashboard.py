import streamlit as st
import pandas as pd
import plotly.express as px


def apply_filters(df):

    filtered = df.copy()

    st.sidebar.header("📌 Dashboard Filters")

    # Category Filter
    cat_cols = filtered.select_dtypes(include=["object", "category"]).columns

    for col in cat_cols:

        values = st.sidebar.multiselect(
            f"{col}",
            filtered[col].dropna().unique(),
            default=filtered[col].dropna().unique(),
            key=f"filter_{col}"
        )

        if len(values):
            filtered = filtered[filtered[col].isin(values)]

    return filtered


def show_kpis(df):

    numeric = df.select_dtypes(include="number").columns

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", len(df))
    c2.metric("Columns", len(df.columns))

    if "Sales" in df.columns:
        c3.metric("Total Sales", f"{df['Sales'].sum():,.2f}")

    else:
        c3.metric("Numeric Columns", len(numeric))

    if "Profit" in df.columns:
        c4.metric("Total Profit", f"{df['Profit'].sum():,.2f}")

    elif len(numeric):
        c4.metric("Mean", round(df[numeric[0]].mean(),2))

    st.divider()


def line_chart(df):

    if "Order_Date" not in df.columns or "Sales" not in df.columns:
        return

    temp=df.copy()

    temp["Order_Date"]=pd.to_datetime(temp["Order_Date"])

    chart=px.line(
        temp,
        x="Order_Date",
        y="Sales",
        title="Sales Trend"
    )

    st.plotly_chart(chart,use_container_width=True)


def bar_chart(df):

    if "Category" not in df.columns or "Sales" not in df.columns:
        return

    chart=px.bar(
        df.groupby("Category")["Sales"].sum().reset_index(),
        x="Category",
        y="Sales",
        color="Category",
        title="Sales by Category"
    )

    st.plotly_chart(chart,use_container_width=True)


def pie_chart(df):

    if "Region" not in df.columns:
        return

    chart=px.pie(
        df,
        names="Region",
        title="Region Distribution"
    )

    st.plotly_chart(chart,use_container_width=True)


def correlation(df):

    numeric=df.select_dtypes(include="number")

    if len(numeric.columns)<2:
        return

    chart=px.imshow(
        numeric.corr(),
        text_auto=True,
        title="Correlation Heatmap"
    )

    st.plotly_chart(chart,use_container_width=True)


def top_records(df):

    st.subheader("Top 10 Records")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True
    )