#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

regex = '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
p = re.compile(regex)
for line in sys.stdin:	    
    try:
	 data = p.match(line.strip()).groups()
    except:
	 continue
    
    if len(data) == 7:
        ip, id, username, date, request, status, size = data
        key = request.split()[1].strip()
	print key,"\t 1"
    	
