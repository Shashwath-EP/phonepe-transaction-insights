import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import json

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(layout="wide")

# ---------------- LOAD DATA ---------------- #
@st.cache_data
def load_data():
    # Connect to SQLite database file
    conn = sqlite3.connect("phonepe.db")

    txn = pd.read_sql("SELECT * FROM aggregated_transaction", conn)
    top = pd.read_sql("SELECT * FROM top_transaction", conn)

    conn.close()
    return txn, top

txn_df, top_df = load_data()

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("Controls")
year = st.sidebar.selectbox("Select Year", sorted(txn_df["year"].unique()))

filtered_txn = txn_df[txn_df["year"] == year]

# ---------------- TITLE ---------------- #
st.title("PhonePe Analytics Dashboard")
st.caption("Interactive Fintech Insights")

# ---------------- KPI ---------------- #
col1, col2 = st.columns(2)

total_txn = int(filtered_txn["count"].sum())
total_amt = filtered_txn["amount"].sum()

col1.metric("Transactions", f"{total_txn:,}")
col2.metric("Amount", f"₹ {total_amt:,.0f}")

# ---------------- TABS ---------------- #
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Geography", "Districts", "Insights"])

# ================= OVERVIEW ================= #
with tab1:

    st.subheader("Top States")

    state_data = (
        filtered_txn.groupby("state")["amount"]
        .sum()
        .reset_index()
        .sort_values(by="amount", ascending=False)
        .head(10)
    )

    fig1 = px.bar(
        state_data,
        x="amount",
        y="state",
        orientation="h",
        color="amount",
        title="Top States"
    )

    fig1.update_layout(
        height=600,
        yaxis=dict(autorange="reversed"),
        plot_bgcolor="#0e1117",
        paper_bgcolor="#0e1117",
        font_color="white"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # -------- Quarterly -------- #
    st.subheader("Quarterly Transactions")

    q_data = filtered_txn.groupby("quarter")["amount"].sum().reset_index()

    fig_q = px.bar(
        q_data,
        x="quarter",
        y="amount",
        color="amount",
        title=f"Quarterly Transactions - {year}"
    )

    fig_q.update_layout(
        height=500,
        plot_bgcolor="#0e1117",
        paper_bgcolor="#0e1117",
        font_color="white"
    )

    st.plotly_chart(fig_q, use_container_width=True)

    # -------- Transaction Types -------- #
    st.subheader("Transaction Types")

    type_data = filtered_txn.groupby("transaction_type")["amount"].sum().reset_index()

    fig2 = px.bar(
        type_data,
        x="amount",
        y="transaction_type",
        orientation="h",
        color="transaction_type",
        title="Transaction Types"
    )

    fig2.update_layout(
        height=500,
        plot_bgcolor="#0e1117",
        paper_bgcolor="#0e1117",
        font_color="white"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ================= MAP ================= #
with tab2:

    st.subheader("India Transaction Gradient Map")

    # Load local GeoJSON
    with open("dashboard/india_states.json") as f:
        geo = json.load(f)

    map_data = filtered_txn.groupby("state")["amount"].sum().reset_index()

    # ---------------- CLEAN DATASET STATES ---------------- #
    map_data["state"] = (
        map_data["state"]
        .str.replace("-", " ")
        .str.replace("&", "and")
        .str.strip()
        .str.lower()
    )

    # FIXES missing states (LOWERCASE VERSION)
    map_data["state"] = map_data["state"].replace({
        "uttarakhand": "uttaranchal",
        "odisha": "orissa"
    })

    # ---------------- CLEAN GEOJSON STATES ---------------- #
    for feature in geo["features"]:
        feature["properties"]["NAME_1"] = (
            feature["properties"]["NAME_1"]
            .replace("&", "and")
            .strip()
            .lower()
        )

    # ---------------- PLOT ---------------- #
    fig_map = px.choropleth(
        map_data,
        geojson=geo,
        locations="state",
        featureidkey="properties.NAME_1",
        color="amount",
        color_continuous_scale="Reds",
        title="Transaction Amount by State"
    )

    fig_map.update_geos(fitbounds="locations", visible=False)

    fig_map.update_layout(
        height=750,
        plot_bgcolor="#0e1117",
        paper_bgcolor="#0e1117",
        font_color="white"
    )

    st.plotly_chart(fig_map, use_container_width=True)

# ================= DISTRICTS ================= #
with tab3:

    st.subheader("Top Districts")

    d_data = (
        top_df[top_df["year"] == year]
        .groupby("district")["amount"]
        .sum()
        .reset_index()
        .sort_values(by="amount", ascending=False)
        .head(15)
    )

    fig3 = px.bar(
        d_data,
        x="amount",
        y="district",
        orientation="h",
        color="amount",
        title="Top Districts"
    )

    fig3.update_layout(
        height=600,
        yaxis=dict(autorange="reversed"),
        plot_bgcolor="#0e1117",
        paper_bgcolor="#0e1117",
        font_color="white"
    )

    st.plotly_chart(fig3, use_container_width=True)

# ================= INSIGHTS ================= #
with tab4:

    st.subheader("Insights")

    top_state = filtered_txn.groupby("state")["amount"].sum().idxmax()

    st.success(f"Top State: {top_state}")
    st.info("Digital payments are increasing steadily")
    st.warning("Few states dominate transaction volume")
