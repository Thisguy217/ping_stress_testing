from pythonping import ping
import csv
import time

Name=input("Name of IP address:")
IP=input('IP address to ping:')

DNS=[Name]
rows = []

for n in range(0,1001):
	cloudflare=ping(IP,count=1,size=(64-8))
	rows.append(cloudflare.rtt_min_ms)
	time.sleep(1)

with open('DNS_Ping_'+Name+'.csv', 'w', newline='') as csvfile:
    write = csv.writer(csvfile)
    write.writerow(DNS)
    write.writerows(map(lambda x: [x], rows))