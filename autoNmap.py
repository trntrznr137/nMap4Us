# Using readline()

import nmap
import os
import sys

nmScan = nmap.PortScanner()

count = 0
print("\nUsing readline()")

PORT_TO_SCAN = "21-443"

rows = []

ipRu = ""

with open(os.path.join(sys.path[0], "LgJkLazF"), "r") as fp:

            
    lines = fp.readlines()

    for line in lines:    
        
        count += 1
        rows = line.split(',')
        ipRu = rows[1]
        ipRu = ipRu.replace('`', '').replace(')', '')


        if not line:
            break

        print("Line {}: nMap4 - {}".format(count, ipRu))

        nmScan.scan(ipRu, PORT_TO_SCAN)

                  




