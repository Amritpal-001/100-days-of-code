import serial
#ser = serial.Serial('/dev/ttyUSB0')  # open serial port
'''print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port'''

arduino = serial.Serial('/dev/ttyUSB0')
while True:  # create loop

    command = str(input("Servo position: "))  # query servo position
    arduino.write(command)  # write position to serial port
    reachedPos = str(arduino.readline())  # read serial port for arduino echo
    print('reachedPos')