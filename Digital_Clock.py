from tkinter import *
from tkinter .ttk import *
from time import strftime
#creating an UI
clock= Tk()
#creating  a title
clock.title("CLock")
def time():
    string=strftime('%H:%M:%S')
    #setting time to label using config
    label.config(text=string)
    #calling  the time function every
    label.after(1000,time)
label = Label(clock, font=('ds-digital', 80), background='black', foreground='cyan')

label.pack(anchor='center')

time()  # Call the time function initially to display the time
clock.mainloop()