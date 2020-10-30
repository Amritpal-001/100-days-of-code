import pyfirmata
from time import sleep
board = pyfirmata.Arduino('/dev/ttyUSB1')

iter8 = pyfirmata.util.Iterator(board)
iter8.start()

# set up pin D9 as Servo Output
pin2 = board.get_pin('d:2:s')
pin3 = board.get_pin('d:3:s')
pin4 = board.get_pin('d:4:s')
pin5 = board.get_pin('d:5:s')

def move_servo(pin , angle):
    pin.write(angle)

move_servo(pin4 , 40)

def sweeping_angle_based(pin , start , end , increment , verbosity = False , RestTime = 0.5):
    current = start
    end = end
    while True:
        while current <= end:
            move_servo(pin , current) # Send data by the port selected
            if verbosity == True:
                print(current)  # See the actual position
            current += increment
        sleep(RestTime)

        while current >= start:
            move_servo(pin , current) # Send data by the port selected
            if verbosity == True:
                print(current)  # See the actual position
            current -= increment
        sleep(RestTime)

sweeping_angle_based(pin2 , 40 , 70 , 10 , verbosity= True)

a = pin2.read()
print(a)

while True:
    print(pin2.read() , pin3.read(), pin4.read(), pin5.read())
    sleep(1)
