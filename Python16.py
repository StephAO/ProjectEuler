#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Stephane
#
# Created:     27-05-2015
# Copyright:   (c) Stephane 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#success
def main():
    n = 2**1000
    print n
    digits = []
    while (n > 0):
        digits.insert(0,n%10)
        n //= 10
    print digits
    print 'sum = ' + str(sum(digits))


if __name__ == '__main__':
    main()
