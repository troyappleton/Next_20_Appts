import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

# ---------- DATABASE CONFIG ----------
DB_CONFIG = {
    'host': '74.208.75.3',
    'database': 'crm_db',
    'user': 'crm_user',
    'password': 'SpaceRace2020!!',
    'port': 3306
}

# ---------- SQL QUERY ----------
QUERY = """
SELECT 
  activity_type,
  city,
  create_uid,
  date_deadline,
  display_name
FROM crm_db.crm_data
WHERE activity_type IN ('Pop-Up', 'Store Visit', 'Meeting', 'KDM Event')
  AND date_deadline <= CURRENT_TIMESTAMP
  AND date_closed != '2020-01-01 00:00:00'
ORDER BY date_deadline DESC
LIMIT 20;
"""

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Today's Tasks", layout="centered")
st.markdown("### 📋 Today's Tasks")

# ---------- LOAD DATA ----------
def load_data():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            df = pd.read_sql(QUERY, connection)
            return df
    except Error as e:
        st.error(f"Database error: {e}")
        return pd.DataFrame()
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

df = load_data()

# ---------- CSS STYLING ----------
st.markdown("""
<style>
.scroll-container {
    max-height: 320px;
    overflow-y: auto;
    padding-right: 10px;
}
.task-card {
    background-color: #f1f1f1;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 8px;
    font-size: 0.85rem;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}
.task-title {
    font-weight: 600;
    margin-bottom: 2px;
}
.task-meta {
    color: #555;
    font-size: 0.75rem;
}
</style>
""", unsafe_allow_html=True)

# ---------- DISPLAY TASKS ----------
if df.empty:
    st.info("No tasks found.")
else:
    st.markdown(f"### Scheduled ({len(df)})")
    st.markdown('<div class="scroll-container">', unsafe_allow_html=True)

    for _, row in df.iterrows():
        icon = "📍" if row["activity_type"] in ["Pop-Up", "Store Visit"] else "💼"
        st.markdown(f"""
        <div class="task-card">
            <div class="task-title">{icon} {row['display_name']}</div>
            <div class="task-meta">{row['activity_type']} • {row['city']} • {row['date_deadline']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
