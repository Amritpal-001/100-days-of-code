
import pyfirmata
from time import sleep

board = pyfirmata.Arduino("/dev/ttyUSB0" , baudrate= 9600)
print('12345')
sleep(1)

def setServoAngle(pin, angle):
  board.digital[pin].write(angle)
  sleep(0.015)

pin = 2
setServoAngle(pin, 80)

'''# Testing the function by rotating motor in both direction
while True:
    for i in range(0, 180):
        setServoAngle(pin, i)
    for i in range(180, 1, -1):
        setServoAngle(pin, i)

    # Continue or break the testing process
    i = input("Enter 'y' to continue or Enter to quit): ")
    if i == 'y':
        pass
    else:
        board.exit()
        break'''


'''# Custom angle to set Servo motor angle
def setServoAngle(pin, angle):
  board.digital[pin].write(angle)
  sleep(0.015)


print('starting')
pin = 5
board.digital[pin].mode = SERVO
board.digital[pin].write(90)
'''



'''print('done')
# start an iterator thread so serial buffer doesn't overflow
iter8 = pyfirmata.util.Iterator(board)
iter8.start()
time.sleep(1)
# set up pin D9 as Servo Output
pin2 = board.get_pin('d:2:s')
time.sleep(1)
print("Button state: %s" % pin2.read())
def move_servo(a):
    pin2.write(a)

move_servo(angle/6)
# set up GUI
root = Tk()

# draw a nice big slider for servo position
scale = Scale(root,
              command=move_servo,
              to=175,
              orient=HORIZONTAL,
              length=400,
              label='Angle')
scale.pack(anchor=CENTER)

# run Tk event loop
root.mainloop()'''