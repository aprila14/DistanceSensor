int potPin = 2;    // select the input pin for the potentiometer
int ledPinbusy = 13;   // select the pin for the LED which indicates "in process/recording" state (green LED)
int ledPinready = 14;   // select the pin for the LED which indicates the "be ready" state (red LED)
int buttonPin = 3 // select the input pin for the button

int val = 0;       // variable to store the value coming from the sensor

void setup() {
  pinMode(ledPinbusy, OUTPUT);  // declare the ledPin as an OUTPUT
  pinMode(ledPinready, OUTPUT);  // declare the ledPin as an OUTPUT
  pinMode(buttonPin, INPUT)
  state = false
}

void loop() {

  while(state == false)
  {
      if(digitalRead(buttonPin) == HIGH)
      {
          digitalWrite(ledPinbusy, LOW);  // turn the ledPinbusy off
          digitalWrite(ledPinready, HIGH)  // turn the ledPinready on
          state = true
      }
  }
  
  while(state == true)
  {
          digitalWrite(ledPinbusy, HIGH);  // turn the ledPinbusy on
          digitalWrite(ledPinready, LOW)  // turn the ledPinready off
          
          val = analogRead(potPin);    // read the value from the sensor
          delay(val);                  // stop the program for some time
          
          
          if(digitalRead(buttonPin) == HIGH)
              {
                  state = false
              }
  }
}