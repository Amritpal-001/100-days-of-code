/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>
Servo myservo1;
Servo myservo2;  // create servo object to control a servo
Servo myservo3;
Servo myservo4; // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  myservo1.attach(2);
  myservo2.attach(11);
  myservo3.attach(10);// attaches the servo on pin 9 to the servo object
}

void loop() {
  for (pos = 30; pos <= 80; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo1.write(pos);
    myservo2.write(pos);
    //myservo3.write(pos);// tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 80; pos >= 30; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo1.write(pos); 
    myservo2.write(pos); 
    //myservo3.write(pos); // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
