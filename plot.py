import matplotlib.pyplot as plt
import csv
import matplotlib

x = []
y = []
n = 10 #it takes every n-th values. n=1 is full resoltuion

with open('datavalues.txt','r') as csvfile:
    data = csv.reader(csvfile, delimiter=';',quoting=csv.QUOTE_NONNUMERIC)
    j=0
    k=0
    for row in data:
        print("number of row: {}".format(len(row)))
        for i in row:
            j=j+1
            #print("j = {}".format(j))
            if (j%n)==0:
                if isinstance(i,float)==True:
                    k=k+1
                    #print("k = {}".format(k))
                    x.append(k)
                    #print(i)
                    y.append((i))


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

#figure 1
ax1.scatter(x,y,1, color='black',label='Federweg')
ax1.set_xlabel('Time [ms]')
ax1.set_ylabel('Federweg [mm]')
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
ax1.set_title('Federweg vs. Zeit')
ax1.legend()

#figure 2
ax2.scatter(x,y,1, color='black',label='Federweg')
ax2.set_xlabel('Time [ms]')
ax2.set_ylabel('Federweg [mm]')
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
ax2.set_title('Federweg vs. Zeit')
ax2.legend()
plt.show()