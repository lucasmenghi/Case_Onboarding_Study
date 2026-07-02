import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="Digital Onboarding Optimization",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

@st.cache_data
def load_data():
    users = pd.read_csv(DATA_DIR / "onboarding_users.csv", parse_dates=["signup_timestamp"])
    support = pd.read_csv(DATA_DIR / "support_calls.csv", parse_dates=["call_timestamp"])
    users["has_support_call"] = users["user_id"].isin(support["user_id"]).astype(int)
    users["upload_now"] = users["upload_choice"].eq("upload_now").astype(int)
    return users, support

users, support = load_data()

st.title("Digital Onboarding Optimization")
st.caption("Synthetic Product Analytics case study")

st.sidebar.header("Filters")

channel = st.sidebar.multiselect(
    "Channel",
    sorted(users["channel"].unique()),
    default=sorted(users["channel"].unique())
)

device = st.sidebar.multiselect(
    "Device",
    sorted(users["device"].unique()),
    default=sorted(users["device"].unique())
)

filtered = users[
    users["channel"].isin(channel)
    & users["device"].isin(device)
].copy()

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Users", f"{len(filtered):,}")
col2.metric("Upload-now", f"{filtered['upload_now'].mean():.1%}")
col3.metric("Submitted", f"{filtered['document_submitted'].mean():.1%}")
col4.metric("Approved", f"{filtered['approved'].mean():.1%}")
col5.metric("Support Rate", f"{filtered['has_support_call'].mean():.1%}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Funnel Conversion")
    funnel = pd.DataFrame({
        "step": ["Started", "P1 Completed", "P2 Reached", "Document Submitted", "Approved"],
        "users": [
            len(filtered),
            filtered["p1_completed"].sum(),
            filtered["p2_reached"].sum(),
            filtered["document_submitted"].sum(),
            filtered["approved"].sum()
        ]
    })
    funnel["conversion_from_start"] = funnel["users"] / max(len(filtered), 1)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(funnel["step"], funnel["conversion_from_start"])
    ax.set_title("Conversion from Start")
    ax.set_ylabel("Rate")
    ax.tick_params(axis="x", rotation=30)
    st.pyplot(fig)

with right:
    st.subheader("Approval by Upload Choice")
    approval = filtered.groupby("upload_choice")["approved"].mean()
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(approval.index, approval.values)
    ax.set_title("Approval Rate")
    ax.set_ylabel("Rate")
    st.pyplot(fig)

st.subheader("Monthly KPI Trends")
monthly = filtered.groupby(filtered["signup_timestamp"].dt.to_period("M").astype(str)).agg(
    upload_now_rate=("upload_now", "mean"),
    approval_rate=("approved", "mean"),
    support_rate=("has_support_call", "mean")
)

fig, ax = plt.subplots(figsize=(12, 4))
monthly.plot(ax=ax, marker="o")
ax.set_title("Monthly KPI Trends")
ax.set_ylabel("Rate")
ax.set_xlabel("Month")
st.pyplot(fig)

st.subheader("Segment Scorecard")
segment = filtered.groupby("channel").agg(
    users=("user_id", "count"),
    upload_now_rate=("upload_now", "mean"),
    approval_rate=("approved", "mean"),
    support_rate=("has_support_call", "mean")
).sort_values("approval_rate", ascending=False)

st.dataframe(segment, use_container_width=True)

st.info(
    "This dashboard uses synthetic data only and is designed for a portfolio case study."
)