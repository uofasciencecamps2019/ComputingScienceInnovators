/* One of sample arduino projects for intro to arduinos

Diagram located at: witAdmin/arduinoProjects/intro/LED-Dimmer.jpg

Code sourced from: http://www.toptechboy.com/arduino/lesson-11-arduino-circuit-to-dim-led-with-potentiometer/

*/

int potPin= A0;  //Declare potPin to be analog pin A0
int LEDPin= 9;  // Declare LEDPin to be arduino pin 9
int readValue;  // Use this variable to read Potentiometer
int writeValue; // Use this variable for writing to LED

void setup() {
  pinMode(potPin, INPUT);  //set potPin to be an input
  pinMode(LEDPin, OUTPUT); //set LEDPin to be an OUTPUT
  Serial.begin(9600);      // turn on Serial Port
}

void loop() {
  
 readValue = analogRead(potPin);  //Read the voltage on the Potentiometer
 writeValue = (255./1023.) * readValue; //Calculate Write Value for LED
 analogWrite(LEDPin, writeValue);      //Write to the LED
 Serial.print("You are writing a value of ");  //for debugging print your values
 Serial.println(writeValue);
 
}
