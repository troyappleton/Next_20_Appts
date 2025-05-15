import streamlit as st
from datetime import datetime

# Sample data (you can replace this with a real query or API call)
tasks = [
    {
        "title": "Call to discuss proposal with Dave",
        "contact": "Dave Wilson",
        "time": "02:15 - 03:00 PM",
        "type": "Call"
    },
    {
        "title": "Intro call",
        "contact": "Diana Scott",
        "time": "05:45 - 04:50 AM",
        "type": "Call"
    },
    {
        "title": "Zoom meeting with Katie",
        "contact": "Katie Bledsoe",
        "time": "12:30 - 01:00 PM",
        "type": "Zoom"
    }
]

# Set page config
st.set_page_config(page_title="Today's Tasks", layout="centered")

# Header
st.markdown("## 📋 Today's Tasks")

# Optional: tag showing how many tasks
st.markdown(f"### Scheduled ({len(tasks)})")

# Custom CSS for card layout
st.markdown("""
<style>
.task-card {
    background-color: #f9f9f9;
    border-radius: 10px;
    padding: 15px 20px;
    margin-bottom: 15px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.task-title {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 5px;
}
.task-meta {
    color: #666;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# Render tasks
for task in tasks:
    icon = "📞" if task["type"].lower() == "call" else "💻"
    st.markdown(f"""
    <div class="task-card">
        <div class="task-title">{icon} {task['title']}</div>
        <div class="task-meta">{task['contact']} • {task['time']}</div>
    </div>
    """, unsafe_allow_html=True)
