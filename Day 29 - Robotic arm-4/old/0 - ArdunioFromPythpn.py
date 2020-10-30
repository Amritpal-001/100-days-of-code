# Control Servo via Zerynth App
from wireless import wifi
from stm.spwf01sa import spwf01sa as wifi_driver   # change the following line to use a different wifi driver
from servo import servo
import streams
from zerynthapp import zerynthapp   # Import the Zerynth APP library

MyServo = servo.Servo(D2.PWM)    # connect the Servo to the pin D2
streams.serial()


degree = 0
sleep(1000)
print("STARTING...")

try:
    '''
    # Device UID and TOKEN can be created in the ADM panel
    zapp = zerynthapp.ZerynthApp("DEVICE UID", "DEVICE TOKEN")
    wifi_driver.init(SERIAL1, D16)  # WiFi Click on slot
    for i in range(0, 5):
        try:
            # connect to the wifi network (Set your SSID and password below)
            wifi.link("SSID", wifi.WIFI_WPA2, "PASSWORD")
            break
        except Exception as e:
            print("Can't link", e)
    else:
        print("Impossible to link!")
        while True:
            sleep(1000)'''

    # Start the Zerynth app instance!
    # Remember to create a template with the files under the "template" folder you just cloned
    # upload it to the ADM and associate it with the connected device
    zapp.run()

    def set_degree(d):
        global degree
        degree = d
        MyServo.moveToDegree(degree)

    zapp.on("set_degree", set_degree)
    while True:
        sleep(50)
        print("degree: ", degree)

except Exception as e:
    print(e)