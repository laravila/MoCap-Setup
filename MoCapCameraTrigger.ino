#include <MsTimer2.h>
const int triggerPin = 2;
const int cameraSyncPin = 7;
boolean flag = LOW;
boolean output = LOW;

void setup() {
  // put your setup code here, to run once:
  MsTimer2::set(20, toogle);
  MsTimer2::start();
  pinMode(triggerPin, OUTPUT);
  pinMode(cameraSyncPin, OUTPUT);

  Serial.begin(9600);

}
void loop() {
  // put your main code here, to run repeatedly:
  char comand;
  if(Serial.available()){
      comand = Serial.read();
      if(comand == 'b'){
          flag = HIGH;
          digitalWrite(triggerPin, HIGH);
          Serial.println("Trigger on");
      }
      if(comand == 's'){
          flag = LOW;
          digitalWrite(triggerPin, LOW);
          Serial.println("Trigger off");
   }
  }
}

void toogle(){
  if(flag == 1){
    digitalWrite(cameraSyncPin, output);
    output = !output;

  }else{
    digitalWrite(cameraSyncPin, LOW);
  }


}
