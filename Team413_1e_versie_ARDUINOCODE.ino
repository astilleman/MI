//---------------------------------Packages invoeren----------------------------------------// Servo - Version: Latest#include <Servo.h>// SoftwareSerial - Version: Latest#include <SoftwareSerial.h>#include <DFRobot_HX711.h>//--------------------------------------Initialisatie variablen------------------------------SoftwareSerial bluetoothSerial(8, 9);int servoPin1 = 6; // Servomotor voor rotatie platformint servoPin2 = 3; // Servomotor voor rotatie weegunitServo servo1; // Create a servo objectServo servo2; // Create a second servo objectint onoff = 0; // start met al de LED's uit// Analoge pinnen (andere pinnen zijn digitaal en worden rechtstreeks in code gebruikt met cijfer)int sensorOut = A0; //Pin voor KLEUROUTint S2S3 = A1; // Pin voor LEDint CLK = A2; // Pin CLK voor gewichtssensorint DOUT = A4; // Pin Data OUT voor gewichtssensorint Mengpin = A3; // Pin voor 5e motor (DC4)int Mosfet4 = A5; // Pin voor relais 4e motor, mengmotor (DC 3)DFRobot_HX711 MyScale(DOUT, CLK);// Default values graanint gewicht_mix = 0;int graan_soort = 0;float zwart_percentage = 0.0;float groen_percentage = 0.0;float geel_percentage = 0.0;// --------------------------------------------setup() en loop () ---------------------------------------------------------void setup(){  servo1.attach(servoPin1); // Attaches the 1st servo on pin D6  servo2.attach(servoPin2); // Attaches the 2nd servo on pin D3   delay(100);  pinMode(S2S3, OUTPUT);  pinMode(sensorOut, INPUT);  delay(100);  bluetoothSerial.begin(9600);  delay(100);  Serial.begin(9600);  MyScale.setCalibration(1992);  delay(100);  servo1.write(45); // Put servo1 at home position   servo2.write(45); // Put servo2 at home postion (eerst mechanisch juist plaatsen, zoadat hoeken kloppen, aangeraden door assistent)  }void loop(){  //Kijk of er iets werd verzonden over bluetooth?  String command = checkBluetooth();   //Voer het commando uit als er iets werd ontvangen  if (command.length()>0){    doCommand(command);  }}  	 //-----------------------------------eigen functies------------------------------------String checkBluetooth() {  //Kijkt of er iets werd verzonden over Bluetooth, ontvangt het en decodeert het ook.  String command = "";  while (bluetoothSerial.available())  {    char c = bluetoothSerial.read();    command += c; // voeg karakter c toe aan command string totdat alle verzonden karakters via bluetoothSerial opgeslagen zijn in command    delay(10);  }  return command;}void doCommand(String command) {  //welk commando werd ontvangen? (eerste karakter)    if (command.startsWith("A")) // LED  {    //Welke parameter werd nog meegestuurd?    String number =  command.substring(1); // splits het commando na het eerste karakter om de parameters te lezen.    ledControl(onoff);  }  else if (command.startsWith("B")) // Servo1 voor rotatie platform   {    //Welke parameter werd nog meegestuurd?    String number =  command.substring(1); // splits het commando na het eerste karakter om de parameters te lezen.    servoControl1(number.toInt());  }  else if (command.startsWith("D")) // Servo 2 voor rotatie weegunit  {    //Welke parameter werd nog meegestuurd?    String number =  command.substring(1); // splits het commando na het eerste karakter om de parameters te lezen.    servoControl2(number.toInt());  }   else if (command.startsWith("E"))  {    String number =  command.substring(1); // splits het commando na het eerste karakter om de parameters te lezen.    Gewichtssensor();  }   else if (command.startsWith("F"))  {    String number =  command.substring(1); // splits het commando na het eerste karakter om de parameters te lezen.    Kleursensor();  }    else if (command.startsWith("G")) // Totale gewicht mix in gram  {    String number = command.substring(1); // splits het commando na het eerste karakter om de parameters te lezen.    int mix = number.toInt(); //   }   else if (command.startsWith("H")) // Kippenmix  {    String number =  command.substring(1); // splits het commando na het eerste karakter om de parameters te lezen.    int graan_soort = 1;    zwart_percentage = 0.2;    groen_percentage = 0.4;    geel_percentage = 0.4;    int gewicht_graan = SamenstellingGraansoort(gewicht_mix, zwart_percentage, groen_percentage, geel_percentage);    if (gewicht_graan < 0) {    Serial.println("Bestelling compleet!");    return "OK";    }  }    else if (command.startsWith("I")) // Duivenmix  {    String number =  command.substring(1); // splits het commando na het eerste karakter om de parameters te lezen.    int graan_soort = 2;    zwart_percentage = 0.4;    groen_percentage = 0.2;    geel_percentage = 0.4;     int gewicht_graan = SamenstellingGraansoort(gewicht_mix, zwart_percentage, groen_percentage, geel_percentage);    if (gewicht_graan < 0) {    Serial.println("Bestelling compleet!");    return "OK";    }  }     else if (command.startsWith("J")) // Kalkoenmix  {    String number =  command.substring(1); // splits het commando na het eerste karakter om de parameters te lezen.    graan_soort = 3;    zwart_percentage = 0.3;    groen_percentage = 0.1;    geel_percentage = 0.6;    int gewicht_graan = SamenstellingGraansoort(gewicht_mix, zwart_percentage, groen_percentage, geel_percentage);    if (gewicht_graan < 0) {    Serial.println("Bestelling compleet!");    return "OK";    }  }    else if (command.startsWith("K")) //rotatie transportband, 1e motor (DC 1)  {    String number =  command.substring(1);     int gewicht_graan = SamenstellingGraansoort(gewicht_mix, zwart_percentage, groen_percentage, geel_percentage);    int richting = RichtingTransportband(gewicht_graan);    int snelheid = SnelheidTransportband(gewicht_graan);    Motor1_RotatieTransportband(richting, snelheid);  }      else if (command.startsWith("L")) // lineaire actuator, 2e motor (DC 2)  {    String number =  command.substring(1);     int gewicht_graan = SamenstellingGraansoort(gewicht_mix, zwart_percentage, groen_percentage, geel_percentage);    int richting = RichtingLineaireActuator(gewicht_graan);    Motor2_LineaireActuator(richting);  }        else if (command.startsWith("M")) // Rotatie platform, 3e motor (servo 1)  {    String number =  command.substring(1);    int gewicht_graan = SamenstellingGraansoort(gewicht_mix, zwart_percentage, groen_percentage, geel_percentage);    int hoek_platform = Motor3_RotatiePlatfrom_Hoek(gewicht_graan);  }      else if (command.startsWith("N")) // Menger inladen en uitladen, 4e motor (DC 3)  {    String number =  command.substring(1);     int richting = RichtingMengstaaf();    int snelheid = 150; // Voorlopig constante snelheid    Motor4_Menger_heen_en_weer(richting, snelheid);  }      else if (command.startsWith("O")) // Mengen graan in graanbak, 5e motor (DC 4)  {    String number =  command.substring(1);     Motor5_Mengen_in_graanbak();  }      else if (command.startsWith("P")) // Rotatie weegunit van 0 tot 90° en terug, 6e motor (servo 2)  {    String number =  command.substring(1);    int gewicht_graan = SamenstellingGraansoort(gewicht_mix, zwart_percentage, groen_percentage, geel_percentage);    int hoek_platform = Motor3_RotatiePlatfrom_Hoek(gewicht_graan);    int hoek_weegunit = Motor6_RotatieWeegunit_Hoek(gewicht_graan, hoek_platform);  }  else if (command == "1") { //LED aan    onoff = 1;    ledControl(onoff);  }  else if (command  == "0") { // LED uit    onoff = 0;    ledControl(onoff);  }  Serial.println("Ontvangen commando: " + command);}void ledControl(int aanuit) {  // zet LEDje aan/uit  digitalWrite(S2S3, aanuit);}void servoControl1(int servoPWM) {  servo1.write(servoPWM);}void servoControl2(int servoPWM) {  servo2.write(servoPWM);}void Gewichtssensor(){Serial.print(MyScale.readWeight(), 1);Serial.println(" g");delay(200);}//Berekent benodigde gewicht van de graansoortint SamenstellingGraansoort(int gewicht_mix, float zwart_percentage, float groen_percentage, float geel_percentage) {  if (graan_soort == 1) {  float gewicht_graan = zwart_percentage * gewicht_mix;  return gewicht_graan;  }  else if (graan_soort == 2) {  float gewicht_graan = groen_percentage * gewicht_mix;  return gewicht_graan;  }  else {  float gewicht_graan = geel_percentage * gewicht_mix;  return gewicht_graan;  }}void Kleursensor(){  int frequency = 0;  frequency = pulseIn(sensorOut, LOW);  if (frequency < 1700) {   // tussen 200 en 1800 (ongeveer volgens wat de assistent zich herinnert)  // zwart rond 1800 (of hoger))    digitalWrite(S2S3,LOW);  }}/* Informatie 1e motor (DC 1):PWM D5. Met relais verbonden.Relais aangestuurd door Mosfet2 op pin D4. Relais krijgt stroom van LDO */// Bepaalt of transportband naar voor of achter moet draaien op basis van gewicht graanint RichtingTransportband(int gewicht_graan){  int gewogen_gewicht = MyScale.readWeight();  if (gewogen_gewicht < gewicht_graan){  int richting =  1;  digitalWrite(4, HIGH);  return richting;  }  else{  int richting = 0;  digitalWrite(4, LOW);  return richting;  }}// Snelheid transportband op basis van gewicht graanint SnelheidTransportband(int gewicht_graan){ int gewogen_gewicht = MyScale.readWeight(); if (gewogen_gewicht == gewicht_graan){ return 0; } else if (gewicht_graan>= (3*gewogen_gewicht)/4){ return 250; } else if (gewicht_graan >= (gewogen_gewicht)/8){ return 125; } else{ return 50; }  }void Motor1_RotatieTransportband(int richting, int snelheid){  pinMode(5, OUTPUT);  analogWrite(5, snelheid);  delay(6000);  analogWrite(5, 0);}/* Informatie 2e motor (DC 2):Duur nog nader te bepalen door mechanica-teamPin D11. Motor is richtingomkeerbaar via relais. Relais aangestuurd door Mosfet3 op pin D7. */int RichtingLineaireActuator(int gewicht_graan){ /* Tegengestelde richting als  transportband (T: voor-achter, L: achter-voor) */  pinMode(7, OUTPUT);  int gewogen_gewicht = MyScale.readWeight();  if (gewogen_gewicht == gewicht_graan){  int richting =  1;  digitalWrite(7, HIGH);  return richting;  }  else{  int richting = 0;  digitalWrite(7, LOW);  return richting;  }}void Motor2_LineaireActuator(int richting){  pinMode(11, OUTPUT);  digitalWrite(11, HIGH);  delay(6000);  digitalWrite(11, LOW);}/* Informatie 3e motor (servo 1):Duur nog te bepalenPin PWM2 D6. Rotatie hele platform met weegschaal en rolband.*//*Belangrijke opmerking: Eerst motor mechanisch juist plaatsen zodat hoeken kloppen (aangeraden door assistent) */int Motor3_RotatiePlatfrom_Hoek(int gewicht_graan){  int gewogen_gewicht = MyScale.readWeight();  int hoek_platform = 45; // centrale positie servo  if(graan_soort == 1){  hoek_platform = 0;  servo1.write(hoek_platform);  delay(3000);  return hoek_platform;  }  else if (graan_soort == 2){  hoek_platform = 45;  servo1.write(hoek_platform);  delay(3000);  return hoek_platform;  }  else if (graan_soort == 3 && gewicht_graan > gewogen_gewicht){  hoek_platform = 90;  servo1.write(hoek_platform);  delay(3000);  return hoek_platform;  }  else {    hoek_platform = 45; // als al het graan op transportband terug naar centrale positie  return hoek_platform;  servo1.write(hoek_platform);  delay(3000);  }}/* Informatie 4e motor(DC 3)Snelheid nog nader te bepalen door mechanica-team.Voorlopig geen veranderende snelheid (aangeraden door mechanica-team).PWM4 op D10 (wel PWM-pin, indien nodig snelheisveranderend). Relais via Mosfet 4 op A5. Richtingomkeerbare motor. Menger moet heen en weer. */int RichtingMengstaaf(){  pinMode(Mosfet4, OUTPUT);  int gewogen_gewicht = MyScale.readWeight();   if (gewogen_gewicht  != 0){ /* mengstaaf zakt voor zekerheid van zodra er graan   in weegunit is, want weegunit zal waarschijnlijk nooit helemaal leeg zijn */  int richting =  1;  digitalWrite(Mosfet4, HIGH);  return richting;  }  else{  int richting = 0;  digitalWrite(Mosfet4, LOW);  return richting;  }}// Voorlopig constante snelheid dus geen aparte functievoid Motor4_Menger_heen_en_weer(int richting, int snelheid){  pinMode(10, OUTPUT);  analogWrite(10, snelheid);  delay(6000);  analogWrite(10, 0);}/* Informatie 5e motor (DC 4)Pin A3. Niet snelheidscontroleerbaar of richtingscontroleerbaar. */void Motor5_Mengen_in_graanbak(){pinMode(Mengpin, OUTPUT);digitalWrite(Mengpin, HIGH);delay(6000);digitalWrite(Mengpin, LOW);}/* Informatie 6e motor (servo 2)PWM 3 Pin D3Belangrijke opmerking: Eerst motor mechanisch juist plaatsen zodat hoeken kloppen (aangeraden door assistent) */int Motor6_RotatieWeegunit_Hoek(int gewicht_graan, int hoek_platform){  int gewogen_gewicht = MyScale.readWeight();  int hoek_weegunit = 45; // centrale positie servo (zelfde centrale positie als voor transportband)  servo2.write(hoek_weegunit);  if(gewogen_gewicht == gewicht_graan && hoek_platform == 45){  hoek_weegunit = 135; // nog te testen of deze naar links of rechts 90 graden draait  for(hoek_weegunit = 45; hoek_weegunit < 135; hoek_weegunit += 1) {  servo1.write(hoek_weegunit);   delay(10);  }  delay(3000);  int hoek_weegunit_na = 135;  return hoek_weegunit_na;  }  else {  for(hoek_weegunit = 135; hoek_weegunit > 45; hoek_weegunit -= 1) {  servo2.write(hoek_weegunit);   delay(10);  }  delay(3000);  int hoek_weegunit_na = 45;  return hoek_weegunit_na; }}