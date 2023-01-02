import statistics
from tkinter import*
import math
import random
import math
import tkinter as tk
from PIL import Image, ImageTk
import time


# GUI colors defined
purple = "#C55FFC"
neon= "#EFDCF9"
box= "#323E42"
back= "#7954A1"

# configure GUI window
window = Tk(className= "Password Generator")
window.configure(bg= back, padx=30, pady=30)

def gen():

    # get values from text entry boxes
    word = (c1_value.get())
    word2 = (p1_value.get())
    num = (pw1_value.get())
    char = (pw2_value.get())
    password = ''

    word3 = word + word2
    field = (char, word3, num)

    sep = '_'

    field2 = (char, word, num)
    field3 = (char, word2, num)

    password1 = s = "!".join(field)
    password2 = char + num + word3 + char
    password3 = s = "!".join(field2)
    password4 = s = "!".join(field3)

    # display calculated values to ui
    o1.delete("1.0", END)
    o1.insert(END, password1)

    o2.delete("1.0", END)
    o2.insert(END, password2)

    o3.delete("1.0", END)
    o3.insert(END, password3)

    o4.delete("1.0", END)
    o4.insert(END, password4)


# Title and first Left Label
l1 = Label(window, bg=back, fg=purple, text='Password Generator', font='Helvetica 11 bold')
l4 = Label(window, bg=back, fg=neon, text="Enter Two words:", font='Helvetica 9 bold')

# Entry
c1_value = StringVar(window, value='psych')
c1 = Entry(window, bg=neon, fg=box, textvariable=c1_value)
p1_value = StringVar(window, value='blue')
p1 = Entry(window, bg=neon, fg=box, textvariable=p1_value)
t1 = Label(window, bg=back, fg=neon, text='Number and character:', font='Helvetica 9 bold')
pw1_value = StringVar(window, value='5')
pw1 = Entry(window, bg=neon, fg=box, textvariable=pw1_value)
pw2_value = StringVar(window, value='%')
pw2 = Entry(window, bg=neon, fg=box, textvariable=pw2_value)

# padding
s01 = Label(window, bg=back, fg=neon, text='')
s05 = Label(window, bg=back, fg=neon, text='')
s0 = Label(window, bg=back, fg=neon, text='')
s1 = Label(window, bg=back, fg=neon, text='')
s2 = Label(window, bg=back, fg=neon, text='')
s3 = Label(window, bg=back, fg=neon, text='')
s4 = Label(window, bg=back, fg=neon, text='')
s5 = Label(window, bg=back, fg=neon, text='')
s6 = Label(window, bg=back, fg=neon, text='')
s7 = Label(window, bg=back, fg=neon, text='')
s8 = Label(window, bg=back, fg=neon, text='')

# Labels on bg
l5 = Label(window, bg=back, fg=purple, text='Password Options', font='Helvetica 11 bold')
lp2 = Label(window, bg=back, fg=neon, text="Password", font='Helvetica 9 bold')
lp3 = Label(window, bg=back, fg=neon, text="Password", font='Helvetica 9 bold')
l8 = Label(window, bg=back, fg=neon, text="Password", font='Helvetica 9 bold')
l9 = Label(window, bg=back, fg=neon, text="Password", font='Helvetica 9 bold')
l10 = Label(window, bg=back, fg=neon, text="Password", font='Helvetica 9 bold')

# BOXES
o1 = Text(window, bg=neon, fg=back, height=1, width=20)
o2 = Text(window, bg=neon, fg=back, height=1, width=20)
o3 = Text(window, bg=neon, fg=back, height=1, width=20)
o4 = Text(window, bg=neon, fg=back, height=1, width=20)

# Button Widgets Calculate
b1 = Button(window, bg=neon, fg=back, text="Generate", command=gen)

# Grid
l1.grid(row=0, column=1)

# spacing
s01.grid(row=1, column=1)

#Label
l4.grid(row=2, column=0)

# Entry
c1.grid(row=2, column=1)
p1.grid(row=2, column=2)

# entry
s05.grid(row=3, column=2)

# Row 4: Widget to display Calculated derivative values
t1.grid(row=4, column=0)
pw1.grid(row=4, column=1)
pw2.grid(row=4, column=2)

# Add Spacing
s0.grid(row=5, column=1)

# Gen button and spacing
b1.grid(row=6, column=1)
s1.grid(row=7, column=1)

# Label Password option centered
l5.grid(row=8, column=1)
s8.grid(row=9, column=0)
l8.grid(row=11, column=0)

# Output Password options
o1.grid(row=11, column=1)
s4.grid(row=12, column=1)
lp2.grid(row=13, column=0)
l9.grid(row=13, column=0)
o2.grid(row=13, column=1)
s5.grid(row=14, column=1)
s2.grid(row=14, column=1)
o3.grid(row=15, column=1)
l10.grid(row=15, column=0)
s6.grid(row=16, column=1)
lp3.grid(row=17, column=0)
o4.grid(row=17, column=1)
# Add Spacing

s3.grid(row=16, column=1)
s7.grid(row=18, column=1)

# Start the GUI
window.mainloop()