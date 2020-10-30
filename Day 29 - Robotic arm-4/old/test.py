import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyUSB0" , baudrate= 9600)
#print('done')
time.sleep(1)
iter8 = pyfirmata.util.Iterator(board)
iter8.start()
#print(iter8)
time.sleep(1)
print(len(board.digital))
time.sleep(1)
servo = board.get_pin('d:2:s')
servo = board.digital[3]
print("Button state: %s" % servo.read())

print(servo)
time.sleep(1)
def move_servo(a):
    servo.write(a)
angle = int(70)
move_servo(angle)
time.sleep(1)
print("Button state: %s" % servo.read())

