#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Stephane
#
# Created:     06-07-2016
# Copyright:   (c) Stephane 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math


def main():
    count = 0
    num = 3
    den = 2
    for i in xrange(1000):
        if int(math.log10(num)) > int(math.log10(den)):
            count += 1
        new_den = num+den
        num = new_den + den
        den = new_den
    print count



if __name__ == '__main__':
    main()
