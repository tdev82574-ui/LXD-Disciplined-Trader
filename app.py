
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import io

st.set_page_config(
    page_title="LXD Disciplined Trader",
    page_icon="📈",
    layout="wide"
)

st.title("📈 LXD Disciplined Trader")
st.caption("AI Trading Discipline Platform")

# --------------------------
# SESSION STATE
# --------------------------

defaults = {
    "started": False,
    "daily_capital": 0.0,
    "max_loss": 0.0,
    "max_trades": 0,
    "trade_count": 0,
    "total_loss": 0.0,
    "cumulative_pnl": 0.0,
    "trade_log": [],
    "discipline_score": 100,
    "locked": False,
    "lock_reason": "",
    "consecutive_losses": 0
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# --------------------------
# PRE-TRADE CHECKLIST
# --------------------------

st.subheader("✅ Pre-Trade Readiness Checklist")

c1 = st.checkbox("I have a clear trading plan")
c2 = st.checkbox("I know my maximum risk today")
c3 = st.checkbox("I am not trying to recover previous losses")
c4 = st.checkbox("I have defined my entry and exit")
c5 = st.checkbox("I am focused and not distracted")

score = sum([c1, c2, c3, c4, c5]) * 20

if score >= 80:
    st.success(f"Readiness Score: {score}/100")
elif score >= 50:
    st.warning(f"Readiness Score: {score}/100")
else:
    st.error(f"Readiness Score: {score}/100")

st.divider()

# --------------------------
# CONFIGURATION
# --------------------------

st.subheader("⚙ Trading Rules")

col1, col2, col3 = st.columns(3)

with col1:
    daily_capital = st.number_input(
        "Daily Capital (USDT)",
        min_value=0.0,
        value=100.0
    )

with col2:
    max_loss = st.number_input(
        "Max Loss Limit (USDT)",
        min_value=0.0,
        value=50.0
    )

with col3:
    max_trades = st.number_input(
        "Max Trades",
        min_value=1,
        value=5
    )

if st.button("🚀 Start Trading Day"):
    st.session_state.started = True
    st.session_state.daily_capital = daily_capital
    st.session_state.max_loss = max_loss
    st.session_state.max_trades = max_trades

    st.success("Trading Day Started Successfully")
