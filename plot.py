import matplotlib.pyplot as plt
import csv

x = []
y = []
n = 10 #it takes every n-th values. n=1 is full resoltuion

with open('datavalues.txt','r') as csvfile:
    data = csv.reader(csvfile, delimiter=';')
    j=0
    k=0
    for row in data:
        print("number of row: {}".format(len(row)))
        for i in row:
            j=j+1
            #print("j = {}".format(j))
            if (j%n)==0:
                k=k+1
                #print("k = {}".format(k))
                x.append(k)
                y.append(float(i))

plt.scatter(x,y,1, color='black',label='Federweg')
plt.xlabel('Time [ms]')
plt.ylabel('Federweg [mm]')
plt.title('Federweg vs. Zeit')
plt.legend()
plt.show()