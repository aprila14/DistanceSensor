#from RPi import GPIO
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

import msvcrt




def animate(i,xs,ys):
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')

#open a file
file1 = open("datavalues.txt","a") 
listen()


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
                temp_c = len
                print(temp_c)
                ani = animation.FuncAnimation(fig, animate,fargs=(len, ys), interval=1000)
                plt.show()
                
                
finally:
        GPIO.cleanup()



file1.close() 

