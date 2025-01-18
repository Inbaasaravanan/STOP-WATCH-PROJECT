#importing tkinter
import tkinter as Tkinter
from datetime import datetime
from tkinter import ttk
counter = 66600
running = False

def counter_label(label):
    def count():
        if running:
            global counter

            if counter==66600:
                display = "Starting..."
            else:
                tt=datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string
            label['text']=display

            label.after(1000, count)
            counter += 1
    count()
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
def Reset(label):
    global counter
    counter = 66600

    if running == False:
        reset['state'] ='disabled'
        label['text']='Welcome!'
    else:
        label['text']="Starting!"
        
inbaa = Tkinter.Tk()
inbaa.title("Stopwatch")

inbaa.minsize(width = 500,height= 100,)
label = Tkinter.Label(inbaa, text="Welcome!", fg="red", font="Verdana 30 bold",bg="pink") 

label.pack()
i=Tkinter.Frame(inbaa)
start = Tkinter.Button(i,text="Start",width = '10', command = lambda:Start(label),bg='orange')
stop = Tkinter.Button(i, text = "Stop", width = '10',state = 'disabled',command=Stop,bg='yellow')
reset = Tkinter.Button(i,text="Reset",width = '10',state='disabled',command= lambda:Reset(label),bg='silver')
i.pack(anchor = 'center', pady = 15)
start.pack(side = "left")
stop.pack(side="left")
reset.pack(side="left")

inbaa.mainloop()
