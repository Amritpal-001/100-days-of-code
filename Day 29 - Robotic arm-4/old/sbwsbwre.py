import pyfirmata

from pyfirmata import Arduino, util
board = Arduino('/dev/ttyUSB0')
servo = board.get_pin('d:10:s')
servo.write(180)        #This works and turns the servo
board.pass_time(1)
servo.write(0)




'''from pyfirmata import Arduino, u+til
board = Arduino('/dev/ttyUSB0')

servo = board.get_pin('d:11:s')
servo.write(180)
'''

'''
board = pyfirmata.Arduino("/dev/ttyUSB0" , baudrate= 9600)
it = pyfirmata.util.Iterator(board)
it.start()

sleep
analog_input = board.get_pin('a:0:i')


while True:

    analog_value = analog_input.read()

    print(analog_value)

    time.sleep(0.1)'''