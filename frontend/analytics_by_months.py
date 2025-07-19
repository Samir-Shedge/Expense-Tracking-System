import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import altair as alt

APP_URL = "https://expense-tracking-system-gew0.onrender.com/"

def analytics_months_tab():
    response = requests.get(f"{APP_URL}/monthly_summary/")
    monthly_summary = response.json()

    df = pd.DataFrame(monthly_summary)
    df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month",
        "year": "Year",
        "total": "Total"
    }, inplace=True)

    # Create Month-Year column and sort
    df["Month-Year"] = pd.to_datetime(df["Year"].astype(str) + "-" + df["Month Number"].astype(str))
    df = df.sort_values(by="Month-Year")

    # For chart display
    df["Month-Year Label"] = df["Month"] + " " + df["Year"].astype(str)

    st.markdown("## 📊 Expense Breakdown by Month")

    # 🎨 Altair Bar Chart
    bar_chart = alt.Chart(df).mark_bar(color="#1f77b4").encode(
        x=alt.X("Month-Year Label:N", sort=df["Month-Year Label"].tolist(), title="Month"),
        y=alt.Y("Total:Q", title="Total Expense"),
        tooltip=[
            alt.Tooltip("Month-Year Label:N", title="Month"),
            alt.Tooltip("Total:Q", title="Total (₹)", format=",.2f")
        ]
    ).properties(
        width="container",
        height=400
    ).configure_axis(
        labelAngle=-45
    ).configure_view(
        strokeWidth=0
    )

    st.altair_chart(bar_chart, use_container_width=True)

    # 🧾 Summary Table
    df["Total"] = df["Total"].apply(lambda x: f"₹{x:,.2f}")
    table_df = df[["Month", "Year", "Total"]].set_index(df["Month Number"])
    table_df.index.name = "Month No."

    st.markdown("### 📅 Monthly Summary Table")
    st.dataframe(
        table_df.style.set_properties(**{
            "text-align": "center",
            "font-weight": "bold"
        }).set_table_styles([{
            "selector": "th",
            "props": [("text-align", "center"), ("background-color", "#1f77b4"), ("color", "white")]
        }]),
        use_container_width=True,
        height=450
    )
