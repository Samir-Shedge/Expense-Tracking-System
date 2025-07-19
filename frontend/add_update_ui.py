import streamlit as st
from datetime import datetime
import requests

APP_URL = "https://expense-tracking-system-gew0.onrender.com/"

def add_update_tab():
    st.markdown("## 💸 Add or Update Your Daily Expenses")
    st.markdown("Easily manage up to 7 expense items per day with a modern UI.")

    selected_date = st.date_input("📅 Select Date", datetime(2024, 8, 1))

    try:
        response = requests.get(f"{APP_URL}/expenses/{selected_date}")
        response.raise_for_status()
        existing_expenses = response.json()
    except requests.exceptions.RequestException:
        st.error("❌ Failed to retrieve expenses.")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        st.markdown("### 🧾 Expense Details")

        expenses = []

        for i in range(7):  # Up to 7 entries
            amount = existing_expenses[i]['amount'] if i < len(existing_expenses) else 0.0
            category = existing_expenses[i]['category'] if i < len(existing_expenses) else "Shopping"
            notes = existing_expenses[i]['notes'] if i < len(existing_expenses) else ""

            with st.container():
                with st.expander(f"📌 Expense Entry {i + 1}", expanded=True):  # Always expanded
                    col1, col2, col3 = st.columns([1, 1, 2])
                    with col1:
                        amount_input = st.number_input(
                            "💰 Amount", min_value=0.0, step=1.0,
                            value=amount, key=f"amount_{i}"
                        )
                    with col2:
                        category_input = st.selectbox(
                            "📂 Category", categories,
                            index=categories.index(category), key=f"category_{i}"
                        )
                    with col3:
                        notes_input = st.text_input(
                            "📝 Notes", value=notes, key=f"notes_{i}"
                        )

                    expenses.append({
                        'amount': amount_input,
                        'category': category_input,
                        'notes': notes_input
                    })

        submit_btn = st.form_submit_button("✅ Save Expenses")

        if submit_btn:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]

            try:
                response = requests.post(f"{APP_URL}/expenses/{selected_date}", json=filtered_expenses)
                if response.status_code == 200:
                    st.success("🎉 Expenses updated successfully!")
                    st.balloons()
                else:
                    st.error("⚠️ Failed to update expenses.")
            except requests.exceptions.RequestException:
                st.error("🔌 Network error occurred while updating expenses.")
