import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

APP_URL = "https://expense-tracking-system-gew0.onrender.com/"

def analytics_by_category_tab():
    st.markdown("## 📊 Expense Analytics by Category")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("📅 Start Date:", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("📅 End Date:", datetime(2024, 8, 5))

    st.markdown("")

    if st.button("🚀 Get Analytics", use_container_width=True):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{APP_URL}/analytics/", json=payload)
        response = response.json()

        if not response:
            st.warning("No data available for the selected date range.")
            return

        data = {
            "Category": list(response.keys()),
            "Total": [response[category]['total'] for category in response],
            "Percentage": [response[category]["percentage"] for category in response]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        # 🎨 Pie Chart for Category-wise Expense %
        fig = px.pie(df_sorted,
                     names='Category',
                     values='Percentage',
                     title='💡 Expense Distribution by Category',
                     color_discrete_sequence=px.colors.sequential.RdBu,
                     hole=0.4)
        st.plotly_chart(fig, use_container_width=True)

        # 📈 Horizontal Bar Chart using Plotly
        fig_bar = px.bar(df_sorted,
                         x="Percentage",
                         y="Category",
                         orientation='h',
                         color='Category',
                         title="📌 Percentage Contribution by Category",
                         color_discrete_sequence=px.colors.qualitative.Bold)
        fig_bar.update_layout(yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_bar, use_container_width=True)

        # 🎯 Beautiful Table
        df_sorted["Total"] = df_sorted["Total"].map("₹{:,.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}%".format)
        st.markdown("### 📋 Detailed Table")
        st.dataframe(df_sorted.style)