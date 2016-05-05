#!/usr/bin/python

import sys

totalHits = 0
oldKey = ''
#1-file name 2- total count
maxFile = ['', 0]
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        if totalHits > maxFile[1]:
		maxFile[0] = oldKey
		maxFile[1] = totalHits
        oldKey = thisKey;
        totalHits = 0

    oldKey = thisKey
    totalHits += float(thisValue)

if oldKey != None:
    if totalHits > maxFile[1]:
                maxFile[0] = thisKey
                maxFile[1] = totalHits

print maxFile[0],'\t',maxFile[1]

