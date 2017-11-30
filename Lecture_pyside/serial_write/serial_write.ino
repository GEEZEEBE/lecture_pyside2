#define LED 13
void setup(){
  Serial.begin(9600);
  pinMode(LED, OUTPUT); 
  digitalWrite(LED, LOW);  
}
void loop(){
  if (Serial.available()) {   
    char c = Serial.read();
    Serial.print("digital LED status : ");      
    Serial.print(c);      
    if(c == '1'){
        digitalWrite(LED, HIGH);  
        Serial.println(digitalRead(LED));      
    }
    if(c == '0'){
        digitalWrite(LED, LOW);  
        Serial.println(digitalRead(LED));      
    }
  }
}
