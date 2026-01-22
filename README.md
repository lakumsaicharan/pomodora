# 🍅 Pomodoro Timer

A productivity timer application based on the Pomodoro Technique, built with Python's tkinter library. Stay focused and manage your time effectively with structured work sessions and breaks.

## 📝 Description

The Pomodoro Timer is a desktop application that implements the famous Pomodoro Technique for time management. It helps you maintain focus during work sessions and ensures you take regular breaks to stay productive throughout the day. The app features a beautiful tomato icon and visual progress tracking.

## ✨ Features

- ⏱️ **25-minute work sessions** for focused productivity
- ☕ **5-minute short breaks** between work sessions
- 🌟 **20-minute long break** after 4 completed work sessions
- ✅ **Visual checkmarks** to track completed work sessions
- 🍅 **Tomato icon display** (classic Pomodoro symbol)
- 🎨 **Color-coded timer states** (Green for work, Pink/Red for breaks)
- 🔄 **Reset functionality** to start fresh
- ⏰ **Real-time countdown** display in MM:SS format
- 📱 **Clean and intuitive GUI** with minimal design

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **tkinter** - Standard GUI library for Python
- **math** - For time calculations

## 📁 Project Structure

```
pomodora/
├── main.py          # Main application with timer logic
├── tomato.png       # Tomato icon for visual display
├── LICENSE          # MIT License
└── README.md        # Project documentation
```

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lakumsaicharan/pomodora.git
   cd pomodora
   ```

2. **No additional dependencies required!**
   - tkinter comes pre-installed with Python
   - Ensure tomato.png is in the same directory as main.py

## 💻 Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Using the timer:**
   - Click **"Start"** to begin a work session
   - The timer will automatically alternate between work and breaks
   - Click **"Reset"** to stop and restart the timer
   - Watch checkmarks appear as you complete work sessions

### Pomodoro Cycle

```
Work (25 min) → Short Break (5 min) → Work (25 min) → Short Break (5 min) →
Work (25 min) → Short Break (5 min) → Work (25 min) → Long Break (20 min) →
[Cycle Repeats]
```

## 🎯 How It Works

### Timer States

| State | Duration | Display Color | Label Text |
|-------|----------|---------------|------------|
| Work Session | 25 minutes | Green | "Work Time" |
| Short Break | 5 minutes | Pink | "Short Break, Chop! Chop!" |
| Long Break | 20 minutes | Red | "Long Break, YAY!" |

### Timer Logic

1. **Work Session (Odd reps):** 25 minutes of focused work
2. **Short Break (Even reps 2, 4, 6):** 5 minutes of rest
3. **Long Break (Rep 8):** 20 minutes of extended rest
4. **Progress Tracking:** Checkmarks (✔) displayed after each completed work session

## 🔧 Code Highlights

### Constants
```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```

### Timer Mechanism
```python
def start_timer():
    global reps
    reps += 1
    if reps%2 != 0:
        count_down(WORK_MIN*60)  # Work session
    elif reps == 8:
        count_down(LONG_BREAK_MIN*60)  # Long break
    else:
        count_down(SHORT_BREAK_MIN*60)  # Short break
```

### Countdown Function
```python
def count_down(count):
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds < 10:
        seconds = f'0{seconds}'
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
```

### Progress Tracking
```python
if reps%2==0:
    work_sessions = int(reps/2)
    check_mark['text'] = "✔"*work_sessions
```

## 📚 Learning Objectives

This project demonstrates:

- ✅ Building timer applications with tkinter
- ✅ Using `window.after()` for scheduled callbacks
- ✅ Canvas widgets for custom graphics
- ✅ PhotoImage for displaying images
- ✅ Global variables for state management
- ✅ Conditional logic for timer states
- ✅ String formatting for time display
- ✅ Dynamic label updates
- ✅ Color schemes and UI design

## 💡 The Pomodoro Technique

Developed by Francesco Cirillo in the late 1980s, the Pomodoro Technique is a time management method that uses a timer to break work into intervals:

1. **Choose a task** you want to work on
2. **Set the timer** to 25 minutes (one Pomodoro)
3. **Work on the task** until the timer rings
4. **Take a short break** (5 minutes)
5. **Every 4 Pomodoros**, take a longer break (15-30 minutes)

### Benefits
- 🎯 Improved focus and concentration
- ⚡ Reduced mental fatigue
- 📊 Better time awareness
- ✅ Increased accountability
- 📈 Enhanced productivity

## 🎨 Customizations

You can easily customize:

### Time Intervals
```python
WORK_MIN = 25        # Change work session duration
SHORT_BREAK_MIN = 5  # Change short break duration
LONG_BREAK_MIN = 20  # Change long break duration
```

### Colors
```python
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
```

### Enhancement Ideas
- Add sound notifications when timer ends
- Include task name input field
- Add statistics tracking (total Pomodoros completed)
- Save session history to a file
- Add pause/resume functionality
- Create settings menu for custom intervals
- Add dark mode theme
- Include motivational quotes

## 📱 Application Window

The app displays:
```
        Timer
    [Tomato Image]
       00:00
  [Start]  [Reset]
        ✔✔
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation
- Share your Pomodoro customizations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Lakum Sai Charan**
- GitHub: [@lakumsaicharan](https://github.com/lakumsaicharan)

## 🌟 Acknowledgments

- Francesco Cirillo for creating the Pomodoro Technique
- Python tkinter documentation
- #100DaysOfCode community
- Tomato icon inspiration

## 📝 Tips for Maximum Productivity

1. **Eliminate distractions** during work sessions
2. **Stand up and stretch** during breaks
3. **Stay hydrated** - keep water nearby
4. **Don't skip breaks** - they're essential for focus
5. **Track your Pomodoros** to measure daily productivity
6. **Adjust intervals** to match your concentration span
7. **Use breaks wisely** - step away from the screen

## 🔍 Troubleshooting

**Issue:** Tomato image not displaying  
**Solution:** Ensure `tomato.png` is in the same directory as `main.py`

**Issue:** Timer not counting down  
**Solution:** Check that no other instance is running

**Issue:** Window not appearing  
**Solution:** Verify tkinter is installed: `python -m tkinter`

---

*Part of my Python learning journey - Day 28 of #100DaysOfCode* 🚀

**Stay focused, stay productive!** 🍅⏱️
