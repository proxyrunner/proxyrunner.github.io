#!/usr/bin/python
# import os
# os.system('clear')
print("\n### | Calculate Named EIGRP Metric | ###\n")

THROUGHPUT = input("Please enter the minimum/slowest THROUGHPUT speed along the path in Kbps(just the number): ")
THROUGHPUT = int(THROUGHPUT)

if THROUGHPUT < 56:
	print('\nProgram Terminating: A minimum link speed of 56Kbps is required!')
	quit()
THROUGHPUT = (10000000 * 65536) / THROUGHPUT
print('After dividing 10^7 by your entered THROUGHPUT value, the K1 value will be: ' + str(THROUGHPUT))
print

LATENCY  = input("\nPlease enter the cumulative LATENCY in picoseconds: ")
LATENCY = int(LATENCY)
LATENCY = (LATENCY * 65536) / 100000
print('After dividing your entered LATENCY value by 10, the K3 value will be: ' + str(LATENCY))

COMPOSITE_METRIC = (THROUGHPUT + LATENCY) 
RIB_SCALE = (COMPOSITE_METRIC  / 128)


print
print("\n\nYour EIGRP metric value is: " + str(COMPOSITE_METRIC))
print("\nUsing a RIB SCALE of 128 results in metric value of: " + str(RIB_SCALE))

print(" \n### | EoF |###\n")
##
## EoF
