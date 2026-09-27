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

# 2. Get current time strictly in UK timezone
uk_timezone = pytz.timezone('Europe/London')
today = datetime.datetime.now(uk_timezone)
year, week_num, day_of_week = today.isocalendar()

# 将今天的日期格式化为类似 "September 27, 2026"
today_str = today.strftime("%B %d, %Y")

# 3. Rotation logic (modulo 5)
offset = 0 
current_index = (week_num + offset) % len(rooms)
current_room = rooms[current_index]

# 4. UI 
st.title("🗑️ Flat Trash Duty Schedule")
st.caption("Fair. Automatic. No Excuses.")

st.divider()

# 显示今天的具体日期
st.markdown(f"### 📅 **Today: {today_str} (Week {week_num})**")

# Highlight current duty
st.success(f"## 🚨 **This Week's Duty: Room {current_room}** 🚨")

# Weekend reminder
if day_of_week in [6, 7]:  # Saturday or Sunday
    st.warning("⚠️ **Weekend Reminder**: Don't forget to take out the main trash bags downstairs on Sunday night ready for the new week!")
    st.balloons()

st.divider()

# 5. Upcoming schedule (加入了具体的日期区间，不再只有枯燥的周数)
st.subheader("🗓️ Upcoming Schedule")

upcoming_schedule = []
# 计算出本周一的日期，以此推算未来几周的具体日期区间
start_of_current_week = today - datetime.timedelta(days=today.weekday())

for i in range(1, 6):
    # 计算未来每周的周一和周日
    future_week_start = start_of_current_week + datetime.timedelta(weeks=i)
    future_week_end = future_week_start + datetime.timedelta(days=6)
    
    f_year, f_week, _ = future_week_start.isocalendar()
    future_room = rooms[(f_week + offset) % len(rooms)]
    
    # 格式化日期区间，例如 "Oct 05 - Oct 11"
    date_range_str = f"{future_week_start.strftime('%b %d')} - {future_week_end.strftime('%b %d')}"
    
    upcoming_schedule.append({
        "Date": date_range_str,
        "Week": f"Week {f_week}",
        "Assigned To": f"Room {future_room}"
    })

st.table(upcoming_schedule)

# Footer
st.caption("💡 Note: The schedule is based on the ISO Week date system and updates automatically every Monday at 00:00 (UK Time).")

