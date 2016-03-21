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
import timeit

#success
def main():
    start = timeit.default_timer();
    sum_of_amicable_numbers = 0
    dict_num_to_sum = {}
    for i in range(2,10000):
        n = find_sum_of_factors(i);
        dict_num_to_sum[i] = n
    for i in dict_num_to_sum:
        n = dict_num_to_sum[i]
        if n in dict_num_to_sum:
            if dict_num_to_sum[n] == i and n != i:
                print str(i) + ' :' + str(dict_num_to_sum[i])
                sum_of_amicable_numbers += i
    print sum_of_amicable_numbers
    stop = timeit.default_timer();
    print stop - start

def find_sum_of_factors(n):
    factors = []
    for f in range(1,n/2 + 1):
        if n%f == 0:
            factors.append(f)
    return sum(factors)


if __name__ == '__main__':
    main()
