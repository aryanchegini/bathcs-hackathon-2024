int in1pin = 65;
int in2pin = 75; // H bridge pins

void setup() {
  pinMode(in1pin, OUTPUT);
  pinMode(in2pin, OUTPUT); // Set motor control pins as outputs
}

void loop() {
  analogWrite(in1pin, 255); // Apply PWM to control speed, 128 out of 255 is about 50% speed
  digitalWrite(in2pin, LOW); // Set the other direction to off

  // The motor will now run continuously in one direction
}
