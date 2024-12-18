void setup() {
  pinMode(13, INPUT);
  pinMode(12, INPUT);
  pinMode(11, INPUT);
  pinMode(10, INPUT);
  
  Serial.begin(9600); // 시리얼 통신 시작
}

void loop() {
  if (digitalRead(10) == HIGH) {
    Serial.println("d"); // 'd' 키 전송
    delay(200); // 디바운싱 처리
  }
  
  if (digitalRead(11) == HIGH) {
    Serial.println("f"); // 'f' 키 전송
    delay(200);
  }
  
  if (digitalRead(12) == HIGH) {
    Serial.println("j"); // 'j' 키 전송
    delay(200);
  }
  
  if (digitalRead(13) == HIGH) {
    Serial.println("k"); // 'k' 키 전송
    delay(200);
  }
}
