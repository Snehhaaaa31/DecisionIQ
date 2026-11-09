
import streamlit as st
import pandas as pd
import plotly.express as px


# =====================================================
# DASHBOARD FILTERS
# =====================================================

def apply_filters(df):

    st.sidebar.header("📌 Dashboard Filters")

    filtered = df

    # Only filter useful categorical columns
    preferred_cols = [
        "Category",
        "Region",
        "Segment",
        "Country",
        "Order_Status",
        "Payment_Method"
    ]

    filter_cols = [
        col for col in preferred_cols if col in df.columns
    ]

    for col in filter_cols:

        values = sorted(df[col].dropna().unique().tolist(), key=str)

        selected = st.sidebar.multiselect(
            col,
            options=values,
            default=values,
            key=f"filter_{col}"
        )

        if len(selected) < len(values):
            filtered = filtered[filtered[col].isin(selected)]

    return filtered


# =====================================================
# KPI CARDS
# =====================================================

def show_kpis(df):

    numeric = df.select_dtypes(include="number").columns

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", f"{len(df):,}")
    c2.metric("Columns", len(df.columns))

    if "Sales" in df.columns:
        c3.metric(
            "Total Sales",
            f"{df['Sales'].sum():,.2f}"
        )
    else:
        c3.metric("Numeric Columns", len(numeric))

    if "Profit" in df.columns:
        c4.metric(
            "Total Profit",
            f"{df['Profit'].sum():,.2f}"
        )
    elif len(numeric):
        c4.metric(
            "Mean",
            f"{df[numeric[0]].mean():,.2f}"
        )


# =====================================================
# SALES TREND
# =====================================================

@st.cache_data(show_spinner=False)
def get_sales_trend(df):

    temp = df[["Order_Date", "Sales"]].copy()

    temp["Order_Date"] = pd.to_datetime(
        temp["Order_Date"],
        errors="coerce"
    )

    temp = temp.dropna()

    result = (
        temp.groupby(
            pd.Grouper(key="Order_Date", freq="MS")
        )["Sales"]
        .sum()
        .reset_index()
    )

    return result


def line_chart(df):

    if "Order_Date" not in df.columns or "Sales" not in df.columns:
        st.info("Order_Date and Sales columns are required for this chart.")
        return

    chart_data = get_sales_trend(df)

    chart = px.line(
        chart_data,
        x="Order_Date",
        y="Sales",
        title="Sales Trend",
        markers=True
    )

    chart.update_layout(
        template="plotly_dark",
        height=400
    )

    st.plotly_chart(chart, use_container_width=True)


# =====================================================
# CATEGORY SALES
# =====================================================

@st.cache_data(show_spinner=False)
def get_category_sales(df):

    return (
        df.groupby("Category", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )


def bar_chart(df):

    if "Category" not in df.columns or "Sales" not in df.columns:
        st.info("Category and Sales columns are required.")
        return

    chart_data = get_category_sales(df)

    chart = px.bar(
        chart_data,
        x="Category",
        y="Sales",
        color="Category",
        title="Sales by Category"
    )

    chart.update_layout(
        template="plotly_dark",
        height=400
    )

    st.plotly_chart(chart, use_container_width=True)


# =====================================================
# REGION DISTRIBUTION
# =====================================================

@st.cache_data(show_spinner=False)
def get_region_distribution(df):

    return df["Region"].value_counts().reset_index(
        name="Count"
    ).rename(columns={"index": "Region"})


def pie_chart(df):

    if "Region" not in df.columns:
        return

    chart_data = get_region_distribution(df)

    chart = px.pie(
        chart_data,
        names="Region",
        values="Count",
        title="Region Distribution",
        hole=0.35
    )

    chart.update_layout(
        template="plotly_dark",
        height=400
    )

    st.plotly_chart(chart, use_container_width=True)


# =====================================================
# CORRELATION HEATMAP
# =====================================================

@st.cache_data(show_spinner=False)
def get_correlation(df):

    numeric = df.select_dtypes(include="number")

    return numeric.corr()


def correlation(df):

    numeric = df.select_dtypes(include="number")

    if len(numeric.columns) < 2:
        st.info("At least two numeric columns are required.")
        return

    corr_data = get_correlation(df)

    chart = px.imshow(
        corr_data,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        title="Correlation Heatmap",
        aspect="auto"
    )

    chart.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(chart, use_container_width=True)


# =====================================================
# TOP 10 RECORDS
# =====================================================

def top_records(df):

    st.subheader("Top 10 Records")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True
    )
