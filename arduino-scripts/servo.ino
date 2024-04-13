#include <Servo.h>
Servo myservo;
Servo notmyservo;
int pos = 0; 
void turnfn() {
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);
    notmyservo.write(pos); // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);
    notmyservo.write(pos);// tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
void setup(){
  myservo.attach(10);
  notmyservo.attach(9);
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop(){
  String message;
  while(!Serial.available());
  message = Serial.readString();
  message.toUpperCase();
  if (message == "T"){
    turnfn();
    }
  Serial.print(message);
}
