import utime
import machine
import uos
import sys
import os
import shutil

import sdcard
import uos

from scd4x_sensirion import SCD4xSensirion
from machine import I2C
from sensor_pack.bus_service import I2cAdapter

from connection import send_data, send_file

#Conversion factor
cf = 3.3/(65535)

#Buzzer
buzz = machine.Pin(15, machine.Pin.OUT)

# Assign chip select (CS) pin (and start it high)
cs = machine.Pin(13, machine.Pin.OUT)

sd_path = "/sd"

# Intialize SPI peripheral (start with 1 MHz)
spi = machine.SPI(1,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(10),
                  mosi=machine.Pin(11),
                  miso=machine.Pin(12))

try:
    # Initialize SD card
    sd = sdcard.SDCard(spi, cs)

    # Mount filesystem
    vfs = uos.VfsFat(sd)
    uos.mount(vfs, "/sd")
except:
    sd_path = ""
    print("oops")
    buzz.value(1)
    utime.sleep(1)
    buzz.value(0)
    

with open(sd_path + '/data_files/data1.csv', 'w') as f:
    f.write("")

#I2C and setup for SCD42
i2c = I2C(1, scl=machine.Pin(3), sda=machine.Pin(2), freq=400000)
adaptor = I2cAdapter(i2c)
sen = SCD4xSensirion(adaptor)
sen.set_measurement(start=False, single_shot=False)
sid = sen.get_id()
t_offs = sen.get_temperature_offset()
sen.set_altitude(sen.get_altitude())
wt = sen.get_conversion_cycle_time()
sen.set_measurement(start=True, single_shot=False)

#Timing for TGS
Vc = machine.Pin(21, machine.Pin.OUT)
Vh = machine.Pin(19, machine.Pin.OUT)

#Switch 
state = machine.Pin(22, machine.Pin.IN)
i = 0
rd = False

#ADC reading for analog sensors
TGS = machine.ADC(27)
TG = machine.ADC(26)

#Because of not working SD, we delete /sd part of path
sd_path = ""

#built in LED
led = machine.Pin(25, machine.Pin.OUT)
led.value(0)	#We make sure that the LED is turned off when the program starts
path = sd_path + "/data_files/test.csv"


#Starting point of new function, currently not working
#for k in range(1, 10):
#    if sd_path + "/data_files/data{}.csv".format(k) not in os.listdir():
#        path = sd_path + "/data_files/data{}.csv".format(k)
#        break
#    else:
#        continue
    


if path == sd_path + "/data_files/test.csv":
    print("UH OH, too much")
    os.remove(sd_path + "/data_files/data1.csv")
    path = sd_path + "/data_files/data1.csv"


#Copying data we saved previously to the other file
with open(sd_path + '/data_files/data1.csv', 'r') as f:
    original_file_contents = f.read()

with open(sd_path + '/data_files/test.csv', 'w') as f:
    f.write(original_file_contents)

#path = sd_path + "/data_files/test.csv" #uncomment to force path
print(path)

if state.value() == 1:
    
    #Clearing the file we save our data in
    with open(sd_path + '/data_files/data1.csv', 'w') as f:
        f.write("")
    
    while True:
        
        #PWM for TGS sensor
        if i == 997 or i == 3997:
           Vc.value(1)
        else:
            Vc.value(0)
    
        if i >= 0 and i <= 1000:
            Vh.value(1)
        else:
            Vh.value(0)
        
        #Switching the value which we read from TGS sensor
        if i == 997:
            TGS_CH4_val = cf*TGS.read_u16()
        elif i == 3997:
            TGS_CO_val = cf*TGS.read_u16()
         
        utime.sleep_ms(5)
        i+=1
        #print(i%(wt/5))
        if i % (wt/5) == 0 and i > 0:
            SCD_CO2_val, SCD_t_val, SCD_rh_val = sen.get_meas_data()
            TG_val = cf*TG.read_u16()
        
            if rd:
                #Data is saved every 5 seconds
                print("CH4: ", TGS_CH4_val, "CO: ", TGS_CO_val, " TG: ", TG_val, " CO2: ", SCD_CO2_val, " T: ", SCD_t_val, " RH: ", SCD_rh_val)
                with open(path, "a") as file:
                    file.write(str(TGS_CH4_val) + ";" + str(TGS_CO_val) + ";" + str(TG_val) + ";" + str(SCD_CO2_val) + ";" + str(SCD_t_val) + ";" + str(SCD_rh_val) + "\n")
                    #file.write(TGS_CH4_val + ";" + TGS_CO_val + ";" + TG_val + ";" + SCD_CO2_val + ";" + SCD_t_val + ";" + SCD_rh_val + "\n")
                    if state.value() == 0:
                        file.close()
                    
                led.toggle()
        
        #If the switch is turned, the program ends
        if state.value() == 0:
            break;
        
        #Device starts gathering data after first full loop (20s)
        if i >=4001:
            i = 0
            rd = True
            
else:
    #Data seding mode, when the data is ready to be sent, it green LED turns on
    led.value(1)
    x = sys.stdin.readline()
    with open(path, "r") as datalog:	#if does not work, change to the previous one
                for line in datalog:
                    #Wait for a command from the host (it's value is never used)
                    x = sys.stdin.readline()
                    print(line)
                datalog.close()
    #When there is no more data to read, green LED turns off
    led.value(0)
    
#Buzzer indicates end of the program
buzz.value(1)
utime.sleep(1)
buzz.value(0)