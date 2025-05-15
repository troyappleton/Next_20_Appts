import streamlit as st

# Sample data (replace with your own source)
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
    },
    {
        "title": "Call with John",
        "contact": "John Appleseed",
        "time": "01:30 - 02:00 PM",
        "type": "Call"
    },
    {
        "title": "Meeting about Q2 goals",
        "contact": "Jane Smith",
        "time": "03:30 - 04:00 PM",
        "type": "Zoom"
    }
]

# Page config
st.set_page_config(page_title="Today's Tasks", layout="centered")

# Title
st.markdown("### 📋 Today's Tasks")

# CSS: smaller card, scrollable container
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

# Scrollable task list
st.markdown('<div class="scroll-container">', unsafe_allow_html=True)

for task in tasks:
    icon = "📞" if task["type"].lower() == "call" else "💻"
    st.markdown(f"""
    <div class="task-card">
        <div class="task-title">{icon} {task['title']}</div>
        <div class="task-meta">{task['contact']} • {task['time']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
