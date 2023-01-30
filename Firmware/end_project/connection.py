#this file contains functions used to communicate between raspberry pi pico and PC

import uos
import sys

def send_file(path):
            with open(path, "r") as datalog:	#if does not work, change to the previous one
                for line in datalog:
                    #wait for a command from the host (it's value is never used)
                    x = sys.stdin.readline().strip()
                    print(line)
                datalog.close()

def send_data(data):
            #wait for a command from the host (it's value is never used)
            x = sys.stdin.readline().strip()
            print(data)
            
def wait_for():
            #wait for a command from the host (it's value is never used)
            x = sys.stdin.readline().strip()
    
def receive_data():
    
        size = 10
        i = 0
    
        with open("settings.txt", "w") as terminal:
                terminal.write("") 
        while i < size:
            with open("settings.txt", "a") as terminal:
                #read a command from the host
                v = sys.stdin.readline().strip()
                terminal.write(str(v) + "\n")
                terminal.close()
                i+=1

