import utime
import machine
import uos
import sys

#ADC0

cf = 3.3/(65535)


Vc = machine.Pin(21, machine.Pin.OUT)
Vh = machine.Pin(19, machine.Pin.OUT)

buzz = machine.Pin(15, machine.Pin.OUT)
tg = 1
i= 0
k = 0



adc_read = machine.ADC(27)


while True:
    
    #if k > 0:
        #adc1 = cf*adc_read.read_u16()
        #print(adc1)
        #print(adc_read.read_u16())
    
    if i == 997 or i == 3997:
        Vc.value(1)
        #adc1 = cf*adc_read.read_u16()
        #print(adc1)
    else:
        Vc.value(0)
    
    if i >= 0 and i <= 1000:
        Vh.value(1)
        adc1 = cf*adc_read.read_u16()
        #print(adc1)
    else:
        Vh.value(0)
        
    buzz.value(tg)   
    
    utime.sleep(0.005)
    tg = (tg + 1)%2
    i+=1
    
    adc1 = cf*adc_read.read_u16()
    
    if adc1 != 3.3:
        print(adc1)
    
    if i >=4001:
        i = 0
        k=1
        buzz.value(1)
        

