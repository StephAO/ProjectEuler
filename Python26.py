#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Stephane
#
# Created:     20-03-2016
# Copyright:   (c) Stephane 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
import time

def main():
    stime = time.clock()
    best_div = -1
    longest_cycle = 0
    for i in reversed(xrange(2,1000)):
        print "-"*20, i, "-"*20
        found = False
        length = 1
        while not found:
            dividend = 1.0
            divisor = i
            cycle = []
            for k in xrange(i):
                result = math.floor(float(dividend*10)/float(divisor))
##                print dividend, divisor, dividend/divisor
                dividend = dividend*10.0 - result*divisor
##                print dividend
##                print result
            for j in xrange(int(math.ceil(2*i/length))*length):
##                print j, length
                numba = int(j/length)
                if (j%length == 0):
                    cycle.append([])

                result = math.floor(dividend*10/divisor)
                dividend = dividend*10.0 - result*divisor
                cycle[numba].append(result)

            check = [cycle[x] == cycle[x+1] for x in range(len(cycle)-1)]
##            print "CYCLE: ", cycle
            if all(check):

                break
            length += 1

        if length > longest_cycle:
            longest_cycle = length
            best_div = i
        if longest_cycle > i:
            break
    print best_div, " with cycle length of :", longest_cycle
    print "time taken: ", time.clock() - stime
if __name__ == '__main__':
    main()
