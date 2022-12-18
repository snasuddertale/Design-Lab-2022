#device notify of its start by blinking three times

from machine import Pin
import utime

led = Pin(25, Pin.OUT)
i = 0

while i <= 5:
    led.toggle()
    utime.sleep(0.5)
    i+=1
