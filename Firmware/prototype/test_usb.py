import sys
import machine

led = machine.Pin(24, machine.Pin.OUT)

def led_on():
    led(1)

def led_off():
    led(0)


while True:
    # read a command from the host
    v = sys.stdin.readline().strip()

    # perform the requested action
    if v.lower() == "on":
        led_on()
    elif v.lower() == "off":
        led_off()