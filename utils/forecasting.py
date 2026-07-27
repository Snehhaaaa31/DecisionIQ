import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from prophet import Prophet


def run_forecast(df, date_col, target_col, periods):

    prophet_df = df[[date_col, target_col]].copy()

    prophet_df.columns = ["ds", "y"]

    prophet_df["ds"] = pd.to_datetime(prophet_df["ds"])

    prophet_df = prophet_df.dropna()

    prophet_df = (
        prophet_df
        .groupby("ds", as_index=False)["y"]
        .sum()
    )

    model = Prophet()

    model.fit(prophet_df)

    future = model.make_future_dataframe(
        periods=periods,
        freq="M"
    )

    forecast = model.predict(future)

    return model, prophet_df, forecast


def show_forecast(prophet_df, forecast):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=prophet_df["ds"],
            y=prophet_df["y"],
            mode="lines+markers",
            name="Actual"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast["ds"],
            y=forecast["yhat"],
            mode="lines",
            name="Forecast"
        )
    )

    fig.update_layout(
        title="Sales Forecast",
        xaxis_title="Date",
        yaxis_title="Value"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_components(model, forecast):

    st.subheader("Trend & Seasonality")

    fig = model.plot_components(forecast)

    st.pyplot(fig)


def show_table(forecast):

    st.subheader("Forecast Data")

    st.dataframe(

        forecast[
            [
                "ds",
                "yhat",
                "yhat_lower",
                "yhat_upper"
            ]
        ].round(2),

        use_container_width=True
    )


def download_forecast(forecast):

    csv = forecast.to_csv(index=False).encode()

    st.download_button(

        "⬇ Download Forecast",

        csv,

        "forecast.csv",

        "text/csv"
    )