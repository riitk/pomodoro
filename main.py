from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    checkmark.config(text='')
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")
    reps = 0
    start["state"] = "normal"

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN*60
    short_break_seconds = SHORT_BREAK_MIN*60
    long_break_seconds = LONG_BREAK_MIN*60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(text="Work")
        count_down(work_seconds)
    elif reps == 2 or reps == 4 or reps == 6:
        timer_label.config(text="Break")
        count_down(short_break_seconds)
    elif reps == 8:
        timer_label.config(text="Break")
        count_down(long_break_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer
    minutes = count//60
    seconds = count % 60

    if start["state"] == "normal":
        start["state"] = "disabled"

    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps//2
        for _ in range (work_sessions):
            marks += "✔"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=80, background=YELLOW)
window.geometry("500x500")

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(104, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)
timer_label = Label(text="Timer", font=("Arial", 30, "bold"), bg=YELLOW, foreground=GREEN)
timer_label.pack_propagate(0)
timer_label.grid(column=1, row=0)


start = Button(text="Start", bg="white", width=7, highlightthickness=0, command=start_timer)
start["state"] = "normal"
start.grid(column=0, row=2)

reset = Button(text="Reset", bg="white", width=7, highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

checkmark = Label(background=YELLOW, foreground=GREEN, font=("Arial", 14, "bold"))
checkmark.grid(column=1, row=3)

window.mainloop()
