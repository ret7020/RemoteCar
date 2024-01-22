/*
Firmware source code for IRC - Internet Remote Car
*/

#include <AFMotor.h> 

AF_DCMotor motor_0(1);
AF_DCMotor motor_1(2);
AF_DCMotor motor_2(3);
AF_DCMotor motor_3(4);

AF_DCMotor motors[4] = {motor_0, motor_1, motor_2, motor_3};

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

void getVals(int *vals, String data, char sep){
  int val_i = 0;
  for(int i=0; i<data.length(); i++){
    if(data[i] == sep){
      val_i++;
      continue;
    }
    vals[val_i] *= 10;
    vals[val_i] += (data[i]-0x30);
  }
}



void loop(){
  if(Serial.available() > 0){

    
   String data = Serial.readStringUntil('\n');
    int vals[3] = {0,0,0};
    getVals(vals, data, ';');
    Serial.println(vals[0]);
    Serial.println(vals[2]);
    if (vals[0] == 0){
      motors[vals[1]].setSpeed(vals[2]); 
      motors[vals[1]].run(FORWARD);
    } else if (vals[0] == 1){
      motors[0].setSpeed(vals[1]);
      motors[1].setSpeed(vals[1]);
      motors[2].setSpeed(vals[1]);
      motors[3].setSpeed(vals[1]);
       
      motors[0].run(FORWARD);
      motors[1].run(FORWARD);
      motors[2].run(FORWARD);
      motors[3].run(FORWARD);
    }
   
    }  

}
