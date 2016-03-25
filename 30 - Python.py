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
import math
import time

def main():
    stime = time.clock()
    nums = []
    for i in range(2,9**5*6):
##        print(i)
        num = i
        total = 0
        while num > 0:
            total += (num%10)**5
            num = math.floor(num/10)
        if total == i:
            nums.append(i)
    print(sum(nums))
    print(time.clock() - stime)
    print(nums)

if __name__ == '__main__':
    main()
