import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_category import analytics_by_category_tab
from analytics_by_month import analytics_month_tab

# ---- Sidebar Design ----
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)  # optional logo
    st.markdown("## 💸 Expense Tracker")
    st.markdown(
        """
        Track, analyze and manage your personal expenses with ease.
        \n📊 Real-time insights by **Category** and **Month**.
        \n🧾 Easy to update and review your spending.
        """
    )

    st.markdown("---")
    st.markdown("**👨‍💻 Developer**: [Samir Shedge](https://www.linkedin.com/in/samir-shedge-9b487327a)")
    st.markdown("**📧 Contact**: samirshedge4153@gmail.com")
    st.markdown("**📅 Version**: 1.0.0")
    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit + FastAPI")

# ---- Page Title and Tabs ----
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 Expense Tracking System")

tab1, tab2, tab3 = st.tabs([
    "➕ Add / Update Expense",
    "📂 Analytics By Category",
    "📆 Analytics By Month"
])

with tab1:
    add_update_tab()

with tab2:
    analytics_by_category_tab()

with tab3:
    analytics_month_tab()
