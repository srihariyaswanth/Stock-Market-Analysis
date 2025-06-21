import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

def make_graph(stock_df, revenue_df, company):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_df['Date'], y=stock_df['Close'], name="Stock Price", line=dict(color='red')))
    fig.update_layout(title=f"{company} Stock Price", xaxis_title="Date", yaxis_title="Price (USD)", template="plotly_white")
    st.plotly_chart(fig)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=revenue_df['Date'], y=revenue_df['Revenue'], name="Revenue", line=dict(color='blue')))
    fig2.update_layout(title=f"{company} Revenue", xaxis_title="Date", yaxis_title="Revenue (USD)", template="plotly_white")
    st.plotly_chart(fig2)

st.title("Stock & Revenue Dashboard")

company = st.selectbox("Select Company", ["Tesla", "GameStop", "Netflix"])

if company == "Tesla":
    revenue = pd.read_csv("tesla_revenue.csv")
    stock = yf.download("TSLA", start="2010-01-01", end="2025-01-01").reset_index()[['Date', 'Close']]
elif company == "GameStop":
    revenue = pd.read_csv("gme_revenue.csv")
    stock = yf.download("GME", start="2010-01-01", end="2025-01-01").reset_index()[['Date', 'Close']]
elif company == "Netflix":
    revenue = pd.read_csv("netflix_revenue.csv")
    stock = yf.download("NFLX", start="2010-01-01", end="2025-01-01").reset_index()[['Date', 'Close']]

revenue['Revenue'] = pd.to_numeric(revenue['Revenue'], errors='coerce')
revenue['Date'] = pd.to_datetime(revenue['Date'])
revenue.dropna(inplace=True)
revenue = revenue.sort_values('Date')
stock['Date'] = pd.to_datetime(stock['Date'])

make_graph(stock, revenue, company)
