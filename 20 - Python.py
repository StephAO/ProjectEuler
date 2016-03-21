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
from math import factorial

#success
def main():
    result = sum(int(x) for x in str(factorial(100)))
    print result

if __name__ == '__main__':
    main()
