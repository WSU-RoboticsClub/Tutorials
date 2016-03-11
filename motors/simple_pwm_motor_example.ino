#define PERIOD_US 1000
#define INPUT_A 7
#define INPUT_B 8

void setup() {
  // put your setup code here, to run once:
  pinMode(INPUT_A, OUTPUT);
  pinMode(INPUT_B, OUTPUT);

  digitalWrite(INPUT_A, LOW);
  digitalWrite(INPUT_B, LOW);
  
}

void loop() {
  // put your main code here, to run repeatedly:

  run_pwm(.5, 0);
 
}

//give a floating-poing value between 0 and 1 for strength
//give an integer (0,1) for direction
void run_pwm(float strength, int direction)
{
  int high_time, low_time;
  int which_pin;

  //check for bad input
  if(strength > 1.0)
  {
    strength = 1.0;
  }
  else if (strength < 0.0)
  {
    strength = 0.0;
  }
  
  //direction logic
  if(direction == 1)
  {
    which_pin = INPUT_A;
  }
  else
  {
    which_pin = INPUT_B;
  }

  //compute delay time for duty cycle
  high_time = strength*PERIOD_US;
  low_time = PERIOD_US - high_time;
  
  digitalWrite(which_pin, HIGH);
  delayMicroseconds(high_time);
  digitalWrite(which_pin, LOW);
  delayMicroseconds(low_time);
  
}

