   
#include <Servo.h>

//SERVO OBJECTS
Servo servo2;
Servo servo3;
Servo servo4;

void setup() {        
  servo2.attach(3);
  servo3.attach(4);
  servo4.attach(5);
  Serial.begin(9600);
}

void loop() {
//Serial.println(180 - servo1.read() ); 
Serial.println(servo2.read()); 
}
