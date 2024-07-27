from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps+=1

    if reps%8==0:
        count_down(LONG_BREAK_MIN*60)
        my_label.config(text="Long Break", fg=RED)
    elif reps %2==0:
        count_down(SHORT_BREAK_MIN*60)
        my_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_min*60) 
        my_label.config(text="Work", fg=GREEN)       
        
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes=count//60
    seconds=count%60
    if seconds<10: # to solve the problem of 24:7 not 24:07
        canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
    else:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    
    if count>0:
        global timer
        timer=window.after(1000, count_down, count-1)
        
    else:
        start_timer()
        marks = ""
        work_sessions =  reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()

window.title("Pomodoro")
window.config(padx=100, pady=80, bg=YELLOW) #bg for background
# ---------------------------- SCALE USED ------------------------------- #
def scale_used(value):
    global work_min
    work_min = int(value)


#Tomato Image
canvas=Canvas(width=200,height=224, bg=YELLOW , highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(103,112, image=tomato_img)
timer_text=canvas.create_text(103,130, text="00:00",fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(row=1,column=2)

#Scale

scale = Scale(from_=0, to=50, command=scale_used)
scale.grid(row=1, column=0)
scale.set(WORK_MIN)

scale_label=Label(text="Set time", fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
scale_label.grid(row=0,column=0)
# Timer and check mark Label

my_label=Label(text="Timer", fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
my_label.grid(row=0, column=2)

check_label=Label( fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
check_label.grid(row=3, column=2)

#Start and Reset Button
start_b=Button(text="Start",highlightthickness=0, command=start_timer) 
start_b.grid(row=2,column=1)

reset_b=Button(text="Reset", highlightthickness=0, command=reset_timer) #command=
reset_b.grid(row=2,column=3)



window.mainloop()