#!/usr/bin/python
# -*- coding: utf-8 -*-
# move a servo from a Tk slider - scruss 2012-10-28

import pyfirmata
from tkinter import *

# don't forget to change the serial port to suit
board = pyfirmata.Arduino('/dev/ttyUSB0')

# start an iterator thread so
# serial buffer doesn't overflow
iter8 = pyfirmata.util.Iterator(board)
iter8.start()

# set up pin D9 as Servo Output
pin2 = board.get_pin('d:2:s')
pin3 = board.get_pin('d:3:s')

def move_servo2(a):
    pin2.write(a)

def move_servo3(a):
    pin3.write(a)

def move_servo4(a):
    pin4.write(a)


# set up GUI
root = Tk()

# draw a nice big slider for servo position
scale = Scale(root,
              command=move_servo2,
              to=175,
              orient=HORIZONTAL,
              length=400,
              label='Angle')

scale1 = Scale(root,
              command=move_servo3,
              to=175,
              orient=HORIZONTAL,
              length=400,
              label='Angle1')


scale.pack(anchor=CENTER)
scale1.pack(anchor=CENTER)

# run Tk event loop
root.mainloop()