#include <Servo.h>

Servo myservo;

const int buttonPin = 4; 
int servoPin = 3;
int in1pin = 6;
int in2pin = 9; // H bridge pins
int buttonState = 0;

void turn() {
  /*
  int pos;
  for (pos = 0; pos <= 90; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 90; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  */
  myservo.write(0);
  delay(1000);
  myservo.write(90);
  delay(1000);
}

void setup() {
  myservo.attach(servoPin);
  myservo.write(90);
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
  Serial.setTimeout(1);
  pinMode(in1pin, OUTPUT);
  pinMode(in2pin, OUTPUT);
  analogWrite(in1pin, LOW);
  analogWrite(in2pin, LOW);
}

void loop() {
  String message;
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
      delay(200);
      Serial.print("b");
    }
  
  if (Serial.available()) {
    message = Serial.readString();
    if (message == "p") {
      analogWrite(in1pin, 200);
      delay(500);
      analogWrite(in1pin, LOW);
      turn();
      analogWrite(in2pin, 255);
      delay(333);
      analogWrite(in2pin, LOW);
    }

    if (message == "g") {
      analogWrite(in2pin, 200);
      delay(500);
      analogWrite(in2pin, LOW);
      turn();
      analogWrite(in1pin, 255);
      delay(333);
      analogWrite(in1pin, LOW);
    }

    if (message == "c") {
      turn();
    }
  
  }
}
