global file
file = None
global rcd
rcd = False
global arrows
arrows = False
global arrowtoggle
def forwardless():
    t.forward(25)
    if rcd == True:
        file.write('t.forward(25)\n')
def backwardless():
    t.backward(25)
    if rcd == True:
        file.write('t.backward(25)\n')
def forward():
    t.forward(50)
    if rcd == True:
        file.write('t.forward(50)\n')
def left():
    t.left(90)
    if rcd == True:
        file.write('t.left(90)\n')
def right():
    t.right(90)
    if rcd == True:
        file.write('t.right(90)\n')
def diagleft():
    t.left(45)
    if rcd == True:
        file.write('t.left(45)\n')
def diagright():
    t.right(45)
    if rcd == True:
        file.write('t.right(45)\n')
def clear():
    t.reset()
    if rcd == True:
        file.write('t.reset()\n')
def backward():
    t.backward(50)
    if rcd == True:
        file.write('t.backward(50)\n')
def lift():
    t.up()
    if rcd == True:
        file.write('t.up()\n')
def drop():
    t.down()
    if rcd == True:
        file.write('t.down()\n')
def green():
    t.color(0, 0.5, 0)
    if rcd == True:
        file.write('t.color(0, 0.5, 0)\n')
def red():
    t.color(1, 0, 0)
    if rcd == True:
        file.write('t.color(1, 0, 0)\n')
def gold():
    t.color(0.9, 0.75, 0)
    if rcd == True:
        file.write('t.color(0.9, 0.75, 0)\n')
def blue():
    t.color(0, 0, 1)
    if rcd == True:
        file.write('t.color(0, 0, 1)\n')
def black():
    t.color(0, 0, 0)
    if rcd == True:
        file.write('t.up()\n')
def begin_fill():
    t.begin_fill()
    if rcd == True:
        file.write('t.begin_fill()\n')
def end_fill():
    t.end_fill()
    if rcd == True:
        file.write('t.end_fill()\n')
def small_circle():
    t.circle(10)
    if rcd == True:
        file.write('t.circle(10)\n')
def medium_circle():
    t.circle(30)
    if rcd == True:
        file.write('t.circle(30)\n')
def large_circle():
    t.circle(50)
    if rcd == True:
        file.write('t.circle(50)\n')
def steepdiagleft():
    t.left(25)
    if rcd == True:
        file.write('t.left(25)\n')
def steepdiagright():
    t.right(25)
    if rcd == True:
        file.write('t.right(25)\n')
def arrowkey():
    global arrows
    global arrowtoggle
    if not arrows:
        arrows = True
        arrowtoggle.config(text="Arrow Key Control: ON")
    else:
        arrows = False
        arrowtoggle.config(text="Arrow Key Control: OFF")
def right(event):
    global arrows
    if arrows:
        t.setheading(0)
        t.forward(5)
def left(event):
    global arrows
    if arrows:
        t.setheading(180)
        t.forward(5)
def up(event):
    global arrows
    if arrows:
        t.setheading(90)
        t.forward(5)
def down(event):
    global arrows
    if arrows:
        t.setheading(270)
        t.forward(5)
def startrcd():
    global rcd
    rcd = True
    global file
    while file == None:
        file = filedialog.asksaveasfile(mode="w", defaultextension=".py")
        if file == None:
            messagebox.showinfo('Recording Canceled', 'No file selected or created.')
            break
    if file != None:
        file.write('import turtle\nturtle.title(\'TDC Save\')\nturtle.setup(width=1000, height=500)\nt = turtle.Pen()\n')
        messagebox.showinfo('Started', 'Recording started.')
def endrcd():
    global rcd
    global file
    if rcd and file != None:
        rcd = False
        file.close()
        file = None
        messagebox.showinfo('Ended', 'Recording ended.')
def close():
    if messagebox.askyesno('Exit?', 'Are you sure you wish to exit?'):
        messagebox.showinfo('Closing', 'TDC is closing.')
        exit()
import turtle
import tkinter.messagebox
from tkinter import filedialog
turtle.setup(width=1000, height=500)
turtle.title('Turtle Design Creator')
t = turtle.Pen()
from tkinter import *
tk = Tk()
tk.title("Toolbox")
a = Button(tk, text="Forward 50", command=forward)
b = Button(tk, text="Left 90", command=left)
c = Button(tk, text="Right 90", command=right)
d = Button(tk, text="Left 45", command=diagleft)
e = Button(tk, text="Right 45", command=diagright)
f = Button(tk, text="Clear", command=clear)
g = Button(tk, text="Backward 50", command=backward)
h = Button(tk, text="Lift", command=lift)
i = Button(tk, text="Drop", command=drop)
j = Button(tk, text="Green", command=green)
k = Button(tk, text="Red", command=red)
l = Button(tk, text="Gold", command=gold)
m = Button(tk, text="Blue", command=blue)
n = Button(tk, text="Black", command=black)
o = Button(tk, text="Begin Fill", command=begin_fill)
p = Button(tk, text="End Fill", command=end_fill)
q = Button(tk, text="Small Circle", command=small_circle)
r = Button(tk, text="Medium Circle", command=medium_circle)
s = Button(tk, text="Large Circle", command=large_circle)
tt = Button(tk, text="Left 25", command=steepdiagleft)
u = Button(tk, text="Right 25", command=steepdiagright)
v = Button(tk, text="Start Recording", command=startrcd)
w = Button(tk, text="End Recording", command=endrcd)
x = Button(tk, text="Exit", command=close)
y = Button(tk, text="Forward 25", command=forwardless)
z = Button(tk, text="Backward 25", command=backwardless)
arrow = Button(tk, text="Arrow Key Control Toggle\n(only 90 degree angles)", command=arrowkey)
arrowtoggle = Label(tk, text="Arrow Key Control: OFF")
a.pack()
b.pack()
c.pack()
d.pack()
e.pack()
f.pack()
g.pack()
h.pack()
i.pack()
j.pack()
k.pack()
l.pack()
m.pack()
n.pack()
o.pack()
p.pack()
q.pack()
r.pack()
s.pack()
tt.pack()
u.pack()
v.pack()
w.pack()
x.pack()
y.pack()
z.pack()
arrow.pack()
arrowtoggle.pack()
tk.bind("<Right>", right)
tk.bind("<Left>", left)
tk.bind("<Up>", up)
tk.bind("<Down>", down)
