
import serial                                       # Modele to use USB ports
import time                                         # Time

arduino = serial.Serial('/dev/ttyUSB0' , 9600, timeout = 1)  # Set up the Conection Arduino - PC
time.sleep(2)                                       # Wait for Arduino
x = 5

'''while x < 90:
    y = (int(x))  # Covertion to Integer Values
    y = str(y)  # Convert it into string
    y = str.encode(y)  # Encoding strings
    arduino.write(y)  # Send data by the port selected
    time.sleep(1.5)  # Delay(s), If you have a servo with quick response decrease the time
    print(x)  # See the actual position
    x += 10
    '''

def sweeping(start , end , increment , verbosity = False):
    current = start
    end = end
    while True:
        while current <= end:
            y = (int(current))  # Covertion to Integer Values
            y = str(y)  # Convert it into string
            y = str.encode(y)  # Encoding strings
            arduino.write(y)  # Send data by the port selected
            time.sleep(1.5)  # Delay(s), If you have a servo with quick response decrease the time
            if verbosity == True:
                print(current)  # See the actual position
            current += increment

        while current >= start:
            y = (int(current))  # Covertion to Integer Values
            y = str(y)  # Convert it into string
            y = str.encode(y)  # Encoding strings
            arduino.write(y)  # Send data by the port selected
            time.sleep(1.5)  # Delay(s), If you have a servo with quick response decrease the time
            if verbosity == True:
                print(current)  # See the actual position
            current -= increment

sweeping(10 , 180 , 10 , verbosity= True)