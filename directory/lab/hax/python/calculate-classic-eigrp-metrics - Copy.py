#!/usr/bin/python
import os
os.system('clear')

BW = input("\n\nPlease enter the minimum/slowest BW speed along the path in Kbps(just the number): ")
BW = int(BW)

if BW < 56:
	print('\nProgram Terminating: A minimum link speed of 56Kbps is required!')
	quit()
BW = 10000000 / BW
print('\nAfter dividing 10^7 by your entered BW value, the K1 value will be: ' + str(BW))
print

DELAY  = input("\n\nPlease enter the cumulative delay in microseconds: ")
DELAY = int(DELAY)
DELAY = DELAY / 10
print('\nAfter dividing your entered DELAY value by 10, the K3 value will be: ' + str(DELAY))

COMPOSITE_METRIC = (BW + DELAY) * 256

print
print("\n\nYour EIGRP metric value is: " + str(COMPOSITE_METRIC) + "\n\n")
##
## EoF
