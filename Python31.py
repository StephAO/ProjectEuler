#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Stephane
#
# Created:     24-03-2016
# Copyright:   (c) Stephane 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time

def main():
    stime = time.clock()
    coins = [200,100,50,20,10,5,2,1]
    num_leaves = 0
    print(branch(200, coins))
    print(time.clock() - stime)

def branch(remainder, coins):
    if remainder==0:
        return 1
    total = 0
    for i in range(len(coins)):
        c = coins[i]
        if c <= remainder:
            total += branch(remainder-c, coins[i:])
    return total


if __name__ == '__main__':
    main()
