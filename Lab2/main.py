import csv
from tariffication import Tariffication
import matplotlib.pyplot as plt
from matplotlib import dates
import datetime as dt
import os

command = "nfdump -r nfcapd.202002251200 'src ip 192.168.250.1 or dst ip 192.168.250.1' -o csv -q > data.csv"
os.system(command)

def lineplot(x_data, y_data, x_label="", y_label="", title=""):
    fmt = dates.DateFormatter('%H:%M:%S')
    _, ax = plt.subplots()
    time_interval = x_data
    time_interval = [dt.datetime.strptime(i, "%H:%M:%S") for i in time_interval]
    ax.plot(time_interval, y_data, lw = 2, color = '#216A9C', alpha = 1)
    ax.xaxis.set_major_formatter(fmt)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()

user = Tariffication("192.168.250.1")

with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:

        user.addTrafficIn(row[1], int(row[12]))
        user.addTrafficOut(row[1], int(row[14]))
        user.addTimeVal(row[1], int(row[12]))
        user.addTimeVal(row[1], int(row[14]))

    user.userTariffication()

    times = list(user._time_val.keys())
    val = list(user._time_val.values())

    for i in range(1, len(val)):
        val[i] += val[i-1]

    lineplot(times, val, "time", "bytes", "Value(t)")
































    '''
    fmt = dates.DateFormatter('%H:%M:%S')
    fig, ax = plt.subplots()
    time_interval = times
    time_interval = [dt.datetime.strptime(i, "%H:%M:%S") for i in time_interval]
    plt.plot(time_interval, val)
    ax.xaxis.set_major_formatter(fmt)
    plt.show()
    
    '''
    '''
    fmt = dates.DateFormatter('%H:%M:%S')

    fig, ax = plt.subplots()

    time_interval = times
    time_interval = [dt.datetime.strptime(i, "%H:%M:%S") for i in time_interval]
    print()
    y = val
    x = np.array([x for x in range(5)])
    ax.plot(time_interval, y, "-o")
    #ax.xaxis.set_major_formatter(fmt)
    #fig.autofmt_xdate()
    plt.show()
'''

