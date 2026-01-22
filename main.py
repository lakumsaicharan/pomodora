from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ''

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    label['text'] = "Timer"
    canvas.itemconfig(timer_text,text="00:00")
    check_mark['text'] = ""

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    if reps%2 != 0:
        count_down(WORK_MIN*60)
        label.config(text='Work Time',fg=GREEN,bg=YELLOW)
    elif reps%2 == 0:
        if reps == 8:
            count_down(LONG_BREAK_MIN*60)
            label.config(text='Long Break, YAY!', fg=RED, bg=YELLOW)
        else:
            count_down(SHORT_BREAK_MIN*60)
            label.config(text='Short Break, Chop! Chop!', fg=PINK, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global minutes,seconds
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds < 10:
        seconds = f'0{seconds}'
    canvas.itemconfig(timer_text,text= f'{minutes}:{seconds}')
    if count> 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps%2==0:
            work_sessions = int(reps/2)
            check_mark['text'] = "✔"*work_sessions

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image= tomato)
timer_text = canvas.create_text(103,130, text="00:00",font=(FONT_NAME,35,'bold'), fill="white")
canvas.grid(row=1, column=1)

label = Label(text='Timer',font=(FONT_NAME,40,"bold"),bg=YELLOW,fg=GREEN,highlightthickness=0)
label.grid(row=0, column=1)

button = Button(text="start",font=FONT_NAME,command=start_timer)
button.grid(row= 2, column=0)

button1 = Button(text="Reset",font=FONT_NAME,command=reset)
button1.grid(row= 2,column=2)

check_mark = Label(fg = GREEN,bg= YELLOW)
check_mark.grid(row = 3, column=1)



window.mainloop()