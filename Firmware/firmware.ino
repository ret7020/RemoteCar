#include <AFMotor.h> 

AF_DCMotor motor_0(1);
AF_DCMotor motor_1(2);
AF_DCMotor motor_2(3);
AF_DCMotor motor_3(4);
String command;
AF_DCMotor motors[4] = {motor_0, motor_1, motor_2, motor_3};

String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}


void setup(){
  Serial.begin(115200);
  
  motor_0.setSpeed(255); 
  motor_0.run(RELEASE);
  motor_1.setSpeed(255); 
  motor_1.run(RELEASE);
  motor_2.setSpeed(255); 
  motor_2.run(RELEASE);
  motor_3.setSpeed(255); 
  motor_3.run(RELEASE);
}

void loop(){
  if (Serial.available() > 0) {
    command = Serial.readString();
    String command_id = getValue(command,';',0);
    String command_arg_0 = getValue(command,';',1);
    String command_arg_1 = getValue(command,';',2);
    String command_arg_2 = getValue(command,';',3);
    if (command_id == 0){ // Set
      motors[command_arg_0.toInt()].setSpeed(command_arg_1.toInt()); 
      motors[command_arg_0.toInt()].run(FORWARD);
      
    }

    
  }

}
