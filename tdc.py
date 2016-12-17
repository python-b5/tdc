global file
file = None
global rcd
rcd = False
global arrows
arrows = False
global arrowtoggle
global forward_pixels
global backward_pixels
global left_degrees
global right_degrees
global circle_radius
global cred
global cgreen
global cblue
forward_pixels = 1
backward_pixels = 1
left_degrees = 1
right_degrees = 1
circle_radius = 1
cred = 0
cgreen = 0
cblue = 0
def forwardless():
    t.forward(25)
    if rcd:
        file.write('t.forward(25)\n')
def backwardless():
    t.backward(25)
    if rcd:
        file.write('t.backward(25)\n')
def forward():
    t.forward(50)
    if rcd:
        file.write('t.forward(50)\n')
def left():
    t.left(90)
    if rcd:
        file.write('t.left(90)\n')
def right():
    t.right(90)
    if rcd:
        file.write('t.right(90)\n')
def diagleft():
    t.left(45)
    if rcd:
        file.write('t.left(45)\n')
def diagright():
    t.right(45)
    if rcd:
        file.write('t.right(45)\n')
def clear():
    t.reset()
    if rcd:
        file.write('t.reset()\n')
def backward():
    t.backward(50)
    if rcd:
        file.write('t.backward(50)\n')
def lift():
    t.up()
    if rcd:
        file.write('t.up()\n')
def drop():
    t.down()
    if rcd:
        file.write('t.down()\n')
def green():
    t.color(0, 128, 0)
    if rcd:
        file.write('t.color(0, 128, 0)\n')
def red():
    t.color(255, 0, 0)
    if rcd:
        file.write('t.color(255, 0, 0)\n')
def gold():
    t.color(230, 191, 0)
    if rcd:
        file.write('t.color(230, 191, 0)\n')
def blue():
    t.color(0, 0, 255)
    if rcd:
        file.write('t.color(0, 0, 255)\n')
def black():
    t.color(0, 0, 0)
    if rcd:
        file.write('t.up()\n')
def begin_fill():
    t.begin_fill()
    if rcd:
        file.write('t.begin_fill()\n')
def end_fill():
    t.end_fill()
    if rcd:
        file.write('t.end_fill()\n')
def small_circle():
    t.circle(10)
    if rcd:
        file.write('t.circle(10)\n')
def medium_circle():
    t.circle(30)
    if rcd:
        file.write('t.circle(30)\n')
def large_circle():
    t.circle(50)
    if rcd:
        file.write('t.circle(50)\n')
def steepdiagleft():
    t.left(22.5)
    if rcd:
        file.write('t.left(22.5)\n')
def steepdiagright():
    t.right(22.5)
    if rcd:
        file.write('t.right(22.5)\n')
def arrowkey():
    global arrows
    global arrowtoggle
    if not arrows:
        arrows = True
        arrowtoggle.config(text="Arrow Key Control: ON")
    else:
        arrows = False
        arrowtoggle.config(text="Arrow Key Control: OFF")
def aright(event):
    global arrows
    global rcd
    if arrows:
        t.setheading(0)
        t.forward(5)
        if rcd:
            file.write('t.setheading(0)\nt.forward(5)\n')
def aleft(event):
    global arrows
    global rcd
    if arrows:
        t.setheading(180)
        t.forward(5)
        if rcd:
            file.write('t.setheading(180)\nt.forward(5)\n')
def up(event):
    global arrows
    global rcd
    if arrows:
        t.setheading(90)
        t.forward(5)
        if rcd:
            file.write('t.setheading(90)\nt.forward(5)\n')
def down(event):
    global arrows
    global rcd
    if arrows:
        t.setheading(270)
        t.forward(5)
        if rcd:
            file.write('t.setheading(270)\nt.forward(5)\n')
def custom_forward():
    global forward_pixels
    global rcd
    t.forward(forward_pixels)
    if rcd:
        file.write('t.forward(' + str(forward_pixels) + ')\n')
def custom_backward():
    global backward_pixels
    global rcd
    t.backward(backward_pixels)
    if rcd:
        file.write('t.backward(' + str(backward_pixels) + ')\n')
def custom_left():
    global left_degrees
    global rcd
    t.left(left_degrees)
    if rcd:
        file.write('t.left(' + str(left_degrees) + ')\n')
def custom_right():
    global right_degrees
    global rcd
    t.right(right_degrees)
    if rcd:
        file.write('t.right(' + str(right_degrees) + ')\n')
def custom_circle():
    global circle_radius
    global rcd
    t.circle(circle_radius)
    if rcd:
        file.write('t.circle(' + str(circle_radius) + ')\n')
def custom_color():
    global cred
    global cgreen
    global cblue
    t.color(cred, cgreen, cblue)
    if rcd:
        file.write('t.color(' + str(cred) + ', ' + str(cgreen) + ', ' + str(cblue) + ')\n')
def customset():
    global cforward
    global cbackward
    global cleft
    global cright
    global ccircle
    global r
    global g
    global b
    global customwin
    customwin = Tk()
    customwin.title("Custom Button Settings")
    cforward = Scale(customwin, from_=1, to=1000, label="Forward", length=1000)
    cforward.pack(side=LEFT)
    cforward.set(forward_pixels)
    cbackward = Scale(customwin, from_=1, to=1000, label="Backward", length=1000)
    cbackward.pack(side=LEFT)
    cbackward.set(backward_pixels)
    cleft = Scale(customwin, from_=1, to=360, label="Left", length=360)
    cleft.pack(side=LEFT)
    cleft.set(left_degrees)
    cright = Scale(customwin, from_=1, to=360, label="Right", length=360)
    cright.pack(side=LEFT)
    cright.set(right_degrees)
    ccircle = Scale(customwin, from_=1, to=500, label="Circle", length=500)
    ccircle.pack(side=LEFT)
    ccircle.set(circle_radius)
    r = Scale(customwin, from_=0, to=255, label="Color: Red", length=256)
    r.pack(side=LEFT)
    r.set(cred)
    g = Scale(customwin, from_=0, to=255, label="Color: Green", length=256)
    g.pack(side=LEFT)
    g.set(cgreen)
    b = Scale(customwin, from_=0, to=255, label="Color: Blue", length=256)
    b.pack(side=LEFT)
    b.set(cblue)
    confirm = Button(customwin, text="Apply", command=apply)
    confirm.pack(side=BOTTOM)
def apply():
    global cforward
    global cbackward
    global cleft
    global cright
    global ccircle
    global r
    global g
    global b
    global customwin
    global forward_pixels
    global backward_pixels
    global left_degrees
    global right_degrees
    global circle_radius
    global cred
    global cgreen
    global cblue
    forward_pixels = cforward.get()
    backward_pixels = cbackward.get()
    left_degrees = cleft.get()
    right_degrees = cright.get()
    circle_radius = ccircle.get()
    cred = r.get()
    cgreen = g.get()
    cblue = b.get()
    customwin.destroy()
def custombtn():
    launch = Tk()
    launch.title("Custom Buttons")
    btn_cforward = Button(launch, text="Forward", command=custom_forward)
    btn_cforward.pack()
    btn_cbackward = Button(launch, text="Backward", command=custom_backward)
    btn_cbackward.pack()
    btn_cleft = Button(launch, text="Left", command=custom_left)
    btn_cleft.pack()
    btn_cright = Button(launch, text="Right", command=custom_right)
    btn_cright.pack()
    btn_ccircle = Button(launch, text="Circle", command=custom_circle)
    btn_ccircle.pack()
    btn_ccolor = Button(launch, text="Color", command=custom_color)
    btn_ccolor.pack()
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
        file.write('import turtle\nturtle.title(\'TDC Save\')\nturtle.setup(width=1000, height=500)\nturtle.colormode(255)\nt = turtle.Pen()\n')
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
turtle.colormode(255)
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
tt = Button(tk, text="Left 22.5", command=steepdiagleft)
u = Button(tk, text="Right 22.5", command=steepdiagright)
v = Button(tk, text="Start Recording", command=startrcd)
w = Button(tk, text="End Recording", command=endrcd)
x = Button(tk, text="Exit", command=close)
y = Button(tk, text="Forward 25", command=forwardless)
z = Button(tk, text="Backward 25", command=backwardless)
custom = Button(tk, text="Custom Button Settings", command=customset)
customlaunch = Button(tk, text="Custom Buttons", command=custombtn)
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
custom.pack()
customlaunch.pack()
tk.bind("<Right>", aright)
tk.bind("<Left>", aleft)
tk.bind("<Up>", up)
tk.bind("<Down>", down)
