import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(layout="wide", page_title="Fraud Detection Dashboard")

# Custom dark theme styling
st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: #ffffff;
        }
        .stMetric label, .stMetric div {
            color: #f1c40f;
        }
        .block-container {
            padding: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Experiment: Fraud Detection Dashboard")
st.markdown("---")

col1, col2, col3 = st.columns(3)
col1.metric("Accuracy", "0.97", "+0.01")
col2.metric("Logloss", "0.0111", "-0.0004")
col3.metric("Interpretability", "5", "")

st.markdown("---")

# Gauge-like indicator with plotly
gauge_fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 2,
    title = {"text": "Tuning Iteration"},
    gauge = {
        'axis': {'range': [0, 74]},
        'bar': {'color': "#f1c40f"},
        'bgcolor': "black",
        'borderwidth': 2,
        'bordercolor': "gray",
    },
    number = {'font': {'color': 'white'}}
))
gauge_fig.update_layout(paper_bgcolor="black", font={'color': "#f1c40f"})

roc_fig = go.Figure()
roc_fig.add_trace(go.Scatter(x=[0, 0.1, 1], y=[0, 0.9974, 1], mode='lines+markers', name='ROC Curve'))
roc_fig.update_layout(title='ROC AUC: 0.9974', plot_bgcolor='black', paper_bgcolor='black',
                      font_color='white', xaxis=dict(title='False Positive Rate'),
                      yaxis=dict(title='True Positive Rate'))

feature_data = pd.DataFrame({
    "Feature": [f"f_{i}" for i in range(1, 11)],
    "Importance": [1.0, 0.72, 0.43, 0.34, 0.29, 0.18, 0.14, 0.12, 0.08, 0.06]
})

feature_fig = go.Figure([go.Bar(x=feature_data["Importance"], y=feature_data["Feature"],
                                 orientation='h', marker_color='#f1c40f')])
feature_fig.update_layout(title="Variable Importance",
                          paper_bgcolor='black', plot_bgcolor='black', font_color='white')

col1, col2 = st.columns([1, 2])
col1.plotly_chart(gauge_fig, use_container_width=True)
col2.plotly_chart(roc_fig, use_container_width=True)

st.plotly_chart(feature_fig, use_container_width=True)

st.markdown("---")
st.markdown("**Model**: XGBoost (58 features) | Dataset: payment_fraud_trains.csv → payment_fraud_test.csv")
