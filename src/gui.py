import Tkinter as tk
import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
import time
import random
from collections import deque
import numpy as np
import serial

LARGE_FONT= ("Verdana", 40)
style.use("seaborn-bright")
f = Figure(figsize=(10,6), dpi=100)
a = f.add_subplot(111)
xList1 = deque([0] * 15, maxlen=15)
yList1 = deque([0] * 15, maxlen=15)
xList2 = deque([0] * 15, maxlen=15)
yList2 = deque([0] * 15, maxlen=15)
xList3 = deque([0] * 15, maxlen=15)
yList3 = deque([0] * 15, maxlen=15)
start_time=time.time()
ser = serial.Serial('/dev/tty.usbmodem1562971', 115200)  # open serial port

'Main function to refresh the graph with new points'
def animate(i):

    d=0
    e=0
    f=0

    st=ser.readline()
    if(st!=""):
        tuples=st.split()    

    if(len(tuples)==3):
        d=tuples[0]
        e=tuples[1]
        f=tuples[2]
    
    print d,e,f

    t=time.time()-start_time
    yList1.append(d)
    xList1.append(t)
    yList2.append(e)
    xList2.append(t)
    yList3.append(f)
    xList3.append(t)

    a.clear()
    a.plot(xList1, yList1, "r", label="PS1")
    a.plot(xList2, yList2, "b", label="PS2")
    a.plot(xList3, yList3, "g", label="PS3")
    '''a.legend(bbox_to_anchor=(0,1.02,1,.102), loc=6,
             ncol=2, borderaxespad=0)'''
    a.set_xlabel('Time')
    a.set_ylabel('Current')
    a.set_title("Constant Current Output")

'Function to obtain the values of the sliders current position and print them'
def printsilder(w):
    ser.flushInput()
    ser.flushOutput()
    ser.write(str(w.get()))
    if(ser.readline().decode('ascii')!=""):
        d=(ser.readline().decode('ascii'))
    print(d)

'''Function to define the characteristics of the GUI
including the positions and the number of slider, buttons. There is also
a matplotlib chart embeded into the GUI'''
def widgetwindow(ctr):
    Leftframe = tk.Frame(root)
    Leftframe.pack()
    Rightframe = tk.Frame(root)
    Rightframe.pack(side=tk.RIGHT)

    w1 = tk.Scale(Leftframe, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, length=200)
    w1.grid(row=0)
    w2 = tk.Scale(Leftframe, from_=3.0, to=8.0, resolution=0.1, orient=tk.HORIZONTAL, length=200)
    w2.grid(row=2, column=0)
    MinValue = ttk.Button(Leftframe, text="Set Min Value", command=lambda: printsilder(w1))
    MinValue.grid(row=1, column=0)
    MaxValue = ttk.Button(Leftframe, text="Set Max Value", command=lambda: printsilder(w2))
    MaxValue.grid(row=3, column=0)

    canvas = FigureCanvasTkAgg(f, Rightframe)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    toolbar = NavigationToolbar2TkAgg(canvas, Rightframe)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

root=tk.Tk()
ctr=0
ser = serial.Serial('/dev/tty.usbmodem1562971', 9600)
tk.Tk.wm_title(root,"Prostethic GUI")
widgetwindow(ctr)
ani = animation.FuncAnimation(f, animate, interval=1, frames=range(1,len(xList1)))
root.mainloop()

