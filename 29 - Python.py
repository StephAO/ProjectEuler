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
import itertools as it


def main():
    A = range(2,101)
    B = range(2,101)
    C = it.product(A,B)
    D = set()
    for a,b in C:
        D.add(a**b)
    print(len(D))

if __name__ == '__main__':
    main()
