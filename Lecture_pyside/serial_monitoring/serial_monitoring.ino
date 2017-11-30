int cnt = 0;
void setup(){
  Serial.begin(9600);
}
void loop(){
  Serial.print("Line Count : ");      
  Serial.println(cnt++);      
  delay(50);                     
}
