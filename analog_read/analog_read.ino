int sensorValue1, sensorValue2 = 0;  // variable to store the value coming from the sensor
float volt1, volt2   = 0;

void setup() {
  // declare the ledPin as an OUTPUT:
  Serial.begin(9600);
}

void loop() {
  // read the value from the sensor:
  sensorValue1 = analogRead(A0);
  sensorValue2 = analogRead(A1);
  
  // stop the program for <sensorValue> milliseconds:
  volt1 = sensorValue1*27/1023;
  volt2 = sensorValue2*27/1023;
  Serial.print("Shoulder: ");
  Serial.print(volt1,2);
  Serial.print("  ");
  Serial.print("Elbow: ");
  Serial.println(volt2,2);
  delay(1000);
}
