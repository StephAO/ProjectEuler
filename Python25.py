#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Stephane
#
# Created:     28-05-2015
# Copyright:   (c) Stephane 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

PHI = 1.6180339887498948482043436563811772030917980576

def main():
    i = 2
    r1 = 1
    r2 = 1
    r3 = 0
    while(len(str(r2)) < 1000):
        r3 = r1 + r2
        r1 = r2
        r2 = r3
        i += 1
    print i

def fib(i):
    return int((PHI**i - (-PHI)**(-1))/(5**0.5))




if __name__ == '__main__':
    main()
