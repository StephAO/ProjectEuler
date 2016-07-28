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

# success
from timeit import default_timer as t

def main():
    start = t()
    numbers = set()
    abundant_n = []
    for i in range(1,28123):
        if find_sum_of_factors(i) > i:
            abundant_n.append(i)
            for j in abundant_n:
                if i + j >= 28123:
                    break
                numbers.add(i + j)
    print sum(range(28123))-sum(numbers)

    stop = t()
    print stop - start


def find_sum_of_factors(n):
    factors = set()
    factors.add(1)
    for f in range(2,int(n**0.5) + 1):
        if n%f == 0:
            factors.add(f)
            factors.add(n//f)
    return sum(factors)

if __name__ == '__main__':
    main()
