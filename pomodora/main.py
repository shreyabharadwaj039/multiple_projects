from tkinter import *
import math
YELLOW="#f6c667"
GREEN="#1f6f78"
FONT="Courier"
WORK=25
SHORT_BREAK=5
LONG_BREAK=20
reps=0

def start_timer():
  global reps
  reps+=1
  work=WORK*60
  short=SHORT_BREAK*60
  long=LONG_BREAK*60
  if reps % 8==0:
    count_down(long)
    tilte_label.config(text="Break")
  elif reps % 2==0:
    count_down(short)
    tilte_label.config(text="Break")
  else:
    count_down(work)
    tilte_label.config(text="Work")
    
    
def count_down(count):
  count_min=math.floor(count/60)
  count_sec=count%60
  if count_sec<10:
    count_sec=f"0{count_sec}"
  canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
  if count>0:
    window.after(1000,count_down,count-1)
  
  
    
window=Tk()
window.title("Pomodora")
window.config(padx=100,pady=100,bg=YELLOW)

tilte_label=Label(text="TIMER",fg=GREEN,font=(FONT,30),bg=YELLOW,highlightthickness=0)
tilte_label.grid(column=1,row=0)

canvas=Canvas(width=200,height=200,bg=YELLOW,highlightthickness=0)
timer_text=canvas.create_text(100,100,text="00:00",fill="white",font=(FONT,50,"bold"))
canvas.grid(column=1,row=1)

start=Button(text="Start",command=start_timer)
start.grid(column=0,row=2)

check=Label(text="✅",bg=YELLOW,highlightthickness=0)
check.grid(column=1,row=2)

reset=Button(text="Restart")
reset.grid(column=2,row=2)


window.mainloop()