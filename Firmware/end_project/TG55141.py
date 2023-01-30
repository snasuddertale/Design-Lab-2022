import utime
import machine
import uos
import sys

#ADC0

cf = 3.3/(65535)

adc_read = machine.ADC(26)

while True:
    
    adc0 = cf*adc_read.read_u16()
    
    print(adc0)
    utime.sleep(1)
