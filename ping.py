#!/usr/bin/python3
import csv
import os
from datetime import datetime
from time import sleep
dformat = '%R'
phost='google.com'
pingcsv = open('ping.csv', 'w', newline='')
pingcsv.write('time,ping\n')
writer = csv.writer(pingcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
while True:
    pcache=[]
    cping=os.popen('ping -c 10 ' + phost).read().strip().split('\n')
    for row in cping[1:-4]:
        try:
             pcache.append((float(row.split(' ')[-2].split('=')[1])))
        except:
             pcache.append(0.0)
    pcache=[round(round(sum((pcache)), 2)/len(pcache), 2)]
    writer.writerow([str(datetime.now().strftime(dformat)), float(pcache[0])])
    pingcsv.flush()
    sleep(60)
pingcsv.close()
