import streamlit as st
import datetime
import pytz

# Page configuration
st.set_page_config(
    page_title="Dorm Trash Duty 🗑️",
    page_icon="🗑️",
    layout="centered"
)

# 1. Room list
rooms = ['A', 'B', 'C', 'D', 'E']

# 2. Get current time strictly in UK timezone (handles GMT/BST automatically)
uk_timezone = pytz.timezone('Europe/London')
today = datetime.datetime.now(uk_timezone)
year, week_num, day_of_week = today.isocalendar()

# 3. Rotation logic (modulo 5)
offset = 0 
current_index = (week_num + offset) % len(rooms)
current_room = rooms[current_index]

# 4. UI 
st.title("🗑️ Flat Trash Duty Schedule")
st.caption("Fair. Automatic. No Excuses.")

st.divider()

# Display current week
st.markdown(f"### 📅 **Current: Year {year}, Week {week_num}**")

# Highlight current duty
st.success(f"## 🚨 **This Week's Duty: Room {current_room}** 🚨")

# Weekend reminder
if day_of_week in [6, 7]:  # Saturday or Sunday
    st.warning("⚠️ **Weekend Reminder**: Don't forget to take out the main trash bags downstairs on Sunday night ready for the new week!")
    st.balloons()

st.divider()

# 5. Upcoming schedule (calculating accurate future dates to avoid year-end bugs)
st.subheader("🗓️ Upcoming Schedule")

upcoming_schedule = []
for i in range(1, 6):
    future_date = today + datetime.timedelta(weeks=i)
    f_year, f_week, _ = future_date.isocalendar()
    future_room = rooms[(f_week + offset) % len(rooms)]
    
    upcoming_schedule.append({
        "Week": f"Week {f_week} ({f_year})",
        "Assigned To": f"Room {future_room}"
    })

st.table(upcoming_schedule)

# Footer
st.caption("💡 Note: The schedule is based on the ISO Week date system and updates automatically every Monday at 00:00 (UK Time).")
