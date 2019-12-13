from RPi import GPIO
from time import sleep
import time
import keyboard

#open a file
file1 = open("datavalues.txt","r+") 

clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)


while True:
    print("start")
    try:  # used try so that if user pressed other than the given key error will not be shown
        print("tries")
        if keyboard.is_pressed('A'):  # if key 'q' is pressed 
            print('You Pressed q Key!')
            break  # finishing the loop
        
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
                if dtState != clkState:
                        counter += 1
                else:
                        counter -= 1
        clkLastState = clkState
        len = counter*0.05
        file.write(len+";")


GPIO.cleanup()
file1.close() 

