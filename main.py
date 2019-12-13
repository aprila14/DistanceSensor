#from RPi import GPIO
from time import sleep
import time
import msvcrt


#open a file
file1 = open("datavalues.txt","r+") 


clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xs = []
ys = []
temp_c = 0

len = 0


start = True
try:
        while start == True:
            if msvcrt.kbhit():
                key_stroke = msvcrt.getch()
                if str(key_stroke[0]) == "48":
                    print("start switch to false")
                    start = False
                #print(str(key_stroke[0]))   # will print which key is pressed
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

                
                
finally:
        GPIO.cleanup()

file1.close() 

