#include <stdlib.h>
#include <string>       

//set the baud rate of the USB
void setup()
{
  Serial.begin(115200); // USB is always 12 Mbit/sec
}

//To handle the first task of setting the MIN&MAX current values
void min_max_set(int &ctr)
{
  char arr[99];
  int pos=0;
  while(1)
  {
    //setting up the min value
    while (Serial.available()>0)
    { 
      //Serial.println("inputfound");
      arr[pos++]=Serial.read();
      //delay(500);
      if(Serial.available()==0)
        break;
    }
    if(strlen(arr)!=0)
    {
      //Serial.println("decoding float");
      double readnumber = atof(arr);
      //Serial.println(readnumber,4);
      ctr++;
      //Serial.println(ctr); 
      pos=0;
      memset(&arr[0], 0, sizeof(arr));
      //delay(500);
    }
    //Serial.println("no input");
    if(ctr==2)
      break;
    Serial.println(0);
    //delay(500);
    delay(5);
  }

}

//To handle the second task of sending data to the GUI via USB
//Here we are generating random values and sending it over
void graphing_vals()
{
  
  while(1)
  {
    float t = (float)millis()*1000;
    String x = sin(7*t);
    String y = 5*sin(7*t);
    String z = 10*sin(7*t);
    Serial.println(x+" "+y+" "+z);
    delayMicroseconds(1);
  }
}

//Main control loop
void loop()
{
  int ctr=0;
  min_max_set(ctr);
  if(ctr==2)
    graphing_vals();

}
