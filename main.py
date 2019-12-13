from RPi import GPIO
from time import sleep
import time
import keyboard

#open a file
file = open("datavalues.txt","r+") 

clk = 17
dt = 18
n=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)


while n<100:
    try:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
                if dtState != clkState:
                        counter += 1
                else:
                        counter -= 1
        clkLastState = clkState
        len = counter*0.05
        file.write(str(len)+";")
        n=n+1
    except:
        print("break")
        break

GPIO.cleanup()
file.close()
print("file close and finish")