import serial
import time

import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    if is_admin():
        # Code of your program here

        # open a serial connection
        s = serial.Serial(port="COM3", baudrate=115200)

    else:
        # Re-run the program with admin rights

        # open a serial connection
        s = serial.Serial(port="COM3", baudrate=115200)

        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


    '''
    # blink the led
    while True:
        input("Press Enter to start...")
        s.write(b"ale\n")
        time.sleep(0.2)
        s.write(b"bym\n")
        time.sleep(0.2)
        s.write(b"ten\n")
        time.sleep(0.2)
        s.write(b"sernik\n")
        time.sleep(0.2)
        s.write(b"juz\n")
        time.sleep(0.2)
        s.write(b"zjadl\n")
        time.sleep(0.2)
        s.write(b"on\n")
        time.sleep(0.2)
        s.write(b"off\n")
        time.sleep(1)
        text = s.readline()
        print(text.decode())
        
    '''

    input("Press Enter to start...")
    s.write(b"OK\n")
    while True:


        text = s.readline()
        print(text.decode())
        with open("terminal_data_02.txt", "a") as terminal:
            s.write(b"next\n")
            terminal.write(str(text.decode()))
            terminal.close()
        #time.sleep(0.5)

    '''
    while True:
    
        input("Press Enter to start...")
        s.write(b"ale\n")
        time.sleep(0.2)
        s.write(b"bym\n")
        time.sleep(0.2)
        s.write(b"ten\n")
        time.sleep(0.2)
        s.write(b"sernik\n")
        time.sleep(0.2)
        s.write(b"juz\n")
        time.sleep(0.2)
        s.write(b"zjadl\n")
        time.sleep(0.2)
'''

if __name__ == '__main__':
    main()
