#include <Arduino.h>
#include <HCSR04.h>
#include <BluetoothSerial.h>

BluetoothSerial SerialBT;

UltraSonicDistanceSensor distanceSensor(22, 23);

// put function declarations here:
int myFunction(int, int);

void setup() {
  // put your setup code here, to run once:
  SerialBT.begin("HeadphoneHolder");
  Serial.begin(115200);
}

void loop() {
  long distance = distanceSensor.measureDistanceCm();
  Serial.println(distance);
  SerialBT.println(distance);
  delay(100);
}

