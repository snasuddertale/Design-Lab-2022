import utime
import machine
import uos
import sys

import sdcard

from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

#assign chip select (CS) pin (and start it high)
cs = machine.Pin(1, machine.Pin.OUT)

#initialization of the SPI peripheral for SD card (start with 1 MHz)
spi = machine.SPI(0,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(2),
                  mosi=machine.Pin(3),
                  miso=machine.Pin(4))

path = "/sd/test01.csv" #if card works properly, then sensor data is stored on the sd card

#initialization of the SD card
try:
    sd = sdcard.SDCard(spi, cs)   
    # Mount filesystem
    vfs = uos.VfsFat(sd)
    uos.mount(vfs, "/sd")
except:
    print("SD card is not working, sadly")
    path = "test01.csv" #if card is not working, then the sensor data is stored on the device
    
#initialization of the button (red button on the prototype device); GP 15
btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
#initialization of the swtich (switch with the blue holder); GP 14
sw = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
#initialization of the cable connected to the 3.3V source; if not connected, data is not being saved GPIO 10
sp = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)

#initialization of ADC port for the CO2 Sensor ; ADC0
ptc = machine.ADC(26)
#initialization of the built in thermometer 
tp = machine.ADC(4)
#conversion factor
cf = 3.3/(65535)

print("Running test")

#LCD initialization in I2C
I2C_ADDR     = 0x3F
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

#pin sda connects to GP0 and scl connects to GP5
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(5), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.clear() #clears the LCD
lcd.move_to(0,0) #moves cursor on the LCD to 0,0

#initialization of the built in LED
led = machine.Pin(24, machine.Pin.OUT)

#i = 0 #is defined later
mode = 0 #starting mode is data taking

if not btn.value():
    
    #the red button should be used for setting the mode by holding it long enough
    mode = 1
    lcd.clear()
    lcd.putstr(str(mode)) 
    print(mode)
    utime.sleep(2)
    if not btn.value():
        
        lcd.clear()
        lcd.putstr(str(mode)) 
        
        mode = 2
        print(mode)
        utime.sleep(2)
        
lcd.clear()
lcd.putstr(str(mode)) 
        
print(mode)

#mode = 1 #you can set the mode to be always the one you want

while True:
    if mode == 1:	#data reading mode
        
        lcd.clear()
        lcd.putstr("data sending mode")
        utime.sleep(1)
        
        print("data sending mode")
        
        lcd.clear()
        
        #read a command from the host
        #v = sys.stdin.readline().strip()
        #lcd.putstr(str(v) + "   " + str(i))
        #print(str(v))
        # perform the requested action
    
        #with open("/sd/test01.csv", "r") as datalog:
        with open(path, "r") as datalog:	#if does not work, change to the previous one
            for line in datalog:
                #wait for a command from the host (it's value is never used)
                x = sys.stdin.readline().strip()
                print(line)
            datalog.close()
        break;	#quits the program
    
    elif mode == 2:
        
        lcd.clear()
        lcd.putstr("data receiving mode")
        utime.sleep(1)
        
        print("data receiving mode")
        lcd.clear()
        
        
        '''
        if i == 0:
            res_1 = v
        elif i == 1:
            res_2 = v
        else:
            if v == res_1:
                lcd.clear()
                lcd.putstr("It's on")
            
            elif v == res_2:
                lcd.clear()
                lcd.putstr("It's off")
            
            utime.sleep(1)
        '''
        it = 0
        while it < 8:
            with open("terminal_data_03.txt", "a") as terminal:
                lcd.putstr("file loop") #just for the indication of where the program is
                #read a command from the host
                v = sys.stdin.readline().strip()
                terminal.write(str(v) + "\n")
                terminal.close()
                it+=1
            #utime.sleep(0.5)
        lcd.clear()
        break;
    else:
        
        lcd.clear()
        lcd.putstr("data taking mode")
        utime.sleep(1)
        lcd.clear()
        
        print("data taking mode")
        
        #sets the starting ammount of loops the program makes 
        lim_init = 20
        lim = lim_init
        i = 0

        lcd.move_to(0,0)

        while i < lim:
            vol = ptc.read_u16() * cf	#reads and converts the CO2 sensor voltage
            temp = 27 - (tp.read_u16()*cf - 0.706)/0.001721	#reads and converts the value on the thermometer
    
            lcd.clear()
        
            #it the switch is turned on, the data saved in the file is being deleted
            if sw.value():      
                lcd.putstr("Cleaning . . .")
                while sw.value():
                    with open(path, "w") as file:          
                        file.write("")
                lcd.clear()
            
            #coverting integer data to string  
            Vol = str(vol)
            Temp = str(temp)
    
            #if the button is not pressed, the data is being shown on the LCD screen and saved in the memory
            if btn.value():
                lcd.putstr(Vol + "           " + Temp) 
                if sp.value():	#if the GP10 is connectet do the 3.3V source, the data is being saved
                    with open(path, "a") as file:          
                        file.write(Vol + ";" + Temp +"\n")
            #if the button is being pressed, for each halfs of second is being held, it adds 10 iterations to the loop
            else:
                lim+=10
                lcd.putstr("Elongation:" + " " + str(lim - lim_init))
                utime.sleep(0.5)
    
        
            print(Vol, Temp)
    
            utime.sleep(0.2)
    
            i+=1
        break;
    
    '''
    if i == 0:
        res_1 = v
    elif i == 1:
        res_2 = v
    else:
        if v == res_1:
            lcd.clear()
            lcd.putstr("It's on")
            
        elif v == res_2:
            lcd.clear()
            lcd.putstr("It's off")
            
        utime.sleep(1)
    
    
    with open("terminal_data_02.txt", "a") as terminal:          
            terminal.write(str(v) + "\n")
            terminal.close()
    utime.sleep(0.5)
    '''
    
    #print("aaaAA")
    i+=1	#just incrementation of i

'''



    
print("\n \n \n")
print("-----------")
with open(path, "r") as datalog:
    for line in datalog:
        print(line)
    datalog.close()
print("-----------")


'''