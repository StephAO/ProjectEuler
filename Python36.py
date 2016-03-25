#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Stephane
#
# Created:     25-03-2016
# Copyright:   (c) Stephane 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
import math
def main():
    total = 0
    stime = time.clock()
    for i in range(1000000):
        decimal = i
        binary = bin(i)
        if is_palindrome(str(decimal)) and is_palindrome(str(binary)[2:]):
            total += decimal
    print(total)
    print(time.clock() - stime)

def is_palindrome(string):
    length = len(string)
##    print(string)
    for i in range(math.floor(length/2)):
        if string[i] != string[length-i-1]:
##            print(string[i],string[length-i-1])
            return False
    return True




if __name__ == '__main__':
    main()
