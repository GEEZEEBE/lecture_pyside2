#include <Servo.h>
#define SERVOMOTOR 9

Servo myservo;  

int angle = 0;  
void setup() {
  Serial.begin(9600);
  myservo.attach(SERVOMOTOR); 
}


void loop() {
  if (Serial.available() > 0) {
    angle = Serial.read();
    if(0 <= angle && angle <= 180){
      myservo.write(angle);  
      Serial.print("digital SERVOMOTOR status : ");      
      Serial.println(angle);      
    }
  }
  Serial.flush();
}
