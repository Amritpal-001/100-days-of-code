import serial
#   Linux example
#     usbport = '/dev/ttyUSB0'

usbport = "/dev/ttyUSB0"
ser = serial.Serial(usbport, 9600, timeout=1)

def move(servo, angle):
    '''Moves the specified servo to the supplied angle.
    Arguments:        servo          the servo number to command, an integer from 1-4
                        angle             the desired servo angle, an integer from 0 to 180
    (e.g.) >>> servo.move(2, 90)
           ... # "move servo #2 to 90 degrees"'''

    #angle = str.encode(angle)
    if (0 <= angle <= 180):
        a = '95'
        ser.write(a.encode())
        ser.write(chr(servo))
        ser.write(chr(angle))
    else:
        print("Servo angle must be an integer between 0 and 180.\n")

def init():
    move(1, 70)
    move(2, 70)
    move(3, 70)

init()
