// Video: Kids Video Arcade
// https://www.youtube.com/watch?v=Y6r3-0KQ-Fw
// YouTube Channel: sunnyspeed studio
// Author: Sunny
// Import this to your Arduino board

const int coin_acceptor_signal_pin = 2;
bool is_coin_inserted = false;

void setup() {
  // Open serial connection to communicate the python script on pc
  Serial.begin(9600);

  // attachTnterrupt(): Digital Pins With Interrupts
  
  // The first parameter: is an interrupt number. 
  // Normally you should use digitalPinToInterrupt(pin) to translate 
  // the actual digital pin to the specific interrupt number. 
  // For example, if you connect to pin 2, use digitalPinToInterrupt(2)

  // The second parameter: ISR / Interrupt Service Routine / Interrupt Handler,
  // this is the function to call when the interrupt occurs.
  // This function must have no parameters and return nothing.

  // The third parameter: mode, defines when the interrupt should be triggered
  // RISING to trigger when the pin goes from low to high
  attachInterrupt(digitalPinToInterrupt(coin_acceptor_signal_pin), coinDetected, RISING);
  
  pinMode(coin_acceptor_signal_pin, INPUT);
}

void loop() {
  if (is_coin_inserted)
  {
    // coin detected, send a message via serial
    Serial.println("coin");
    Serial.flush();
    
    // add a delay to register one coin only
    delay(5000);

    // set coin to false, and wait for the next coin
    is_coin_inserted = false;
  }
}

void coinDetected(){
  // coin is detected
  is_coin_inserted = true;
}
