import pyfirmata
import time
board = pyfirmata.Arduino("/dev/ttyUSB0")
print('done')

it = pyfirmata.util.Iterator(board)
it.start()
print('done')
#digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:4:s')
print('done')
while True:
    led.write(60)
    time.sleep(2)
    print('done')
