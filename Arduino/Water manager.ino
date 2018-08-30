// First we include the libraries
#include <OneWire.h> 
#include <DallasTemperature.h>
#include <LiquidCrystal.h>
#include <SPI.h>
#include <Ethernet.h>







int buzzer=10;

const int trigPin = A2;
const int echoPin = A1;
// defines variables
long duration;
int distance;









int i;

// Local Network Settings
byte mac[]     = { 0xD4, 0xA8, 0xE2, 0xFE, 0xA0, 0xA1 }; // Must be unique on local network
byte ip[]      = { 192,168,137 };                // Must be unique on local network


// ThingSpeak Settings
char thingSpeakAddress[] = "api.thingspeak.com";
String writeAPIKey = "H4SWZXM854MNGP6E";    // Write API Key for a ThingSpeak Channel
const int updateInterval = 10000;        // Time interval in milliseconds to update ThingSpeak

// Variable Setup
long lastConnectionTime = 0;
boolean lastConnected = false;
int failedCounter = 0;

// Initialize Arduino Ethernet Client
EthernetClient client;














#define ONE_WIRE_BUS 7
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);





#define SensorPin A3            //pH meter Analog output to Arduino Analog Input 0
#define Offset 0.00            //deviation compensate
#define LED 13
#define samplingInterval 20
#define printInterval 800
#define ArrayLenth  40    //times of collection
int pHArray[ArrayLenth];   //Store the average value of the sensor feedback
int pHArrayIndex=0;    






volatile int FlowPulse; //measuring the rising edges of the signal
int Calc;                               
int flowsensor = 2;










LiquidCrystal lcd(9, 8, 6, 5, 4, 3);










void setup(void) 
{ 
 lcd.begin(20, 4);

 
 Serial.begin(9600); 



    pinMode(buzzer, OUTPUT);
    digitalWrite(buzzer, LOW);


 
 
 Ethernet.begin(mac, ip);
delay(1000);
Serial.print("ETHERNET SHIELD ip  is     : ");
Serial.println(Ethernet.localIP());
// Start Ethernet on Arduino
startEthernet();


attachInterrupt(0, rpm, RISING);



pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
 
 sensors.begin(); 
} 
















void loop(void) 
{ 

  
 sensors.requestTemperatures(); 









  static unsigned long samplingTime = millis();
  static unsigned long printTime = millis();
  static float pHValue,voltage;
  if(millis()-samplingTime > samplingInterval)
  {
      pHArray[pHArrayIndex++]=analogRead(SensorPin);
      if(pHArrayIndex==ArrayLenth)pHArrayIndex=0;
      voltage = avergearray(pHArray, ArrayLenth)*5.0/1024;
      pHValue = 3.5*voltage+Offset;
      samplingTime=millis();
  }
  if(millis() - printTime > printInterval)   //Every 800 milliseconds, print a numerical, convert the state of the LED indicator
  {
        digitalWrite(LED,digitalRead(LED)^1);
        printTime=millis();
  }





  




 
 FlowPulse = 0;      //Set NbTops to 0 ready for calculations
 sei();            //Enables interrupts
 delay (1000);      //Wait 1 second
 cli();            //Disable interrupts
 Calc = (FlowPulse * 60 / 7.5); //(Pulse frequency x 60) / 7.5Q, = flow rate in L/hour 


digitalWrite(trigPin, LOW);
delayMicroseconds(2);
// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);
// Calculating the distance
distance= duration*0.034/2;
// Prints the distance on the Serial Monitor







 lcd.setCursor(0, 0);
 lcd.print("Tempe. is: "); 
 lcd.print(sensors.getTempCByIndex(0));
 String temp2 = String(sensors.getTempCByIndex(0));
 lcd.setCursor(0, 1);
 lcd.print(Calc,DEC);   // print the Flow Rate
 String flow2 = String(Calc);
  lcd.print(" L/m");
 lcd.setCursor(0, 2);
lcd.print("Dist: ");
lcd.println(distance);
String dist = String(distance);

 String date2 = "20180330";
 lcd.setCursor(0, 3);
 lcd.print("pH value: ");
 lcd.println(pHValue,2);
 String ph = String(pHValue);
 String l_id = String(1);
int alerts=0;





if(sensors.getTempCByIndex(0)<20||sensors.getTempCByIndex(0)>40){
  digitalWrite(buzzer, HIGH);
  alerts++;
}
if(Calc<3000||Calc>6000){
  digitalWrite(buzzer, HIGH);
  delay(1000);
  alerts++;
}
if(distance<200||distance>350){
  digitalWrite(buzzer, HIGH);
  delay(1000);
  alerts++;
}
if(pHValue<6||pHValue>8.5){
  digitalWrite(buzzer, HIGH);
  delay(1000);
  alerts++;
}
if(alerts==0){
  digitalWrite(buzzer, LOW);
}
String no_alert=String(alerts);






// Print Update Response to Serial Monitor
if (client.available())
{
char c = client.read();
Serial.print(c);
}
// Disconnect from ThingSpeak
if (!client.connected() && lastConnected)
{
Serial.println();
Serial.println("…disconnected.");
Serial.println();
client.stop();
}
// Update ThingSpeak
if(!client.connected() && (millis()-lastConnectionTime > updateInterval))
{
updateThingSpeak("field1="+temp2+"&field2="+ph+"&field3="+flow2+"&field4="+dist+"&field5="+date2+"&field6="+l_id+"&field7="+no_alert);
}
lastConnected = client.connected();
alerts=0;
} 















void rpm ()     //This is the function that the interupt calls 
{ 
  FlowPulse++;  //This function measures the rising and falling edge of the hall effect sensors signal
} 










double avergearray(int* arr, int number){
  int i;
  int max,min;
  double avg;
  long amount=0;
  if(number<=0){
    Serial.println("Error number for the array to avraging!/n");
    return 0;
  }
  if(number<5){   //less than 5, calculated directly statistics
    for(i=0;i<number;i++){
      amount+=arr[i];
    }
    avg = amount/number;
    return avg;
  }else{
    if(arr[0]<arr[1]){
      min = arr[0];max=arr[1];
    }
    else{
      min=arr[1];max=arr[0];
    }
    for(i=2;i<number;i++){
      if(arr[i]<min){
        amount+=min;        //arr<min
        min=arr[i];
      }else {
        if(arr[i]>max){
          amount+=max;    //arr>max
          max=arr[i];
        }else{
          amount+=arr[i]; //min<=arr<=max
        }
      }//if
    }//for
    avg = (double)amount/(number-2);
  }//if
  return avg;
}










void updateThingSpeak(String tsData)
{
if (client.connect(thingSpeakAddress, 80))
{
client.print("POST /update HTTP/1.1\n");
client.print("Host: api.thingspeak.com\n");
client.print("Connection: close\n");
client.print("X-THINGSPEAKAPIKEY: "+writeAPIKey+"\n");
client.print("Content-Type: application/x-www-form-urlencoded\n");
client.print("Content-Length: ");
client.print(tsData.length());
client.print("\n\n");

client.print(tsData);

lastConnectionTime = millis();

if (client.connected())
{
Serial.println("Connecting to ThingSpeak…");
Serial.println();
client.stop();
failedCounter = 0;
}
else
{
failedCounter++;

Serial.println("Connection to ThingSpeak failed ("+String(failedCounter, DEC)+")");
Serial.println();
client.stop();
}

}
else
{
failedCounter++;

Serial.println("Connection to ThingSpeak Failed ("+String(failedCounter, DEC)+")");
Serial.println();

lastConnectionTime = millis();
client.stop();
}
}

void startEthernet()
{

client.stop();

Serial.println("Connecting Arduino to network…");
Serial.println();

delay(1000);

// Connect to network amd obtain an IP address using DHCP
if (Ethernet.begin(mac) == 0)
{
Serial.println("DHCP Failed, reset Arduino to try again");
Serial.println();
}
else {
Serial.println("Arduino connected to network using DHCP");
Serial.println();
Serial.println("Data being uploaded to THINGSPEAK Server…….");
Serial.println();
}

delay(1000);
}


void ult() {
// Clears the trigPin

}
