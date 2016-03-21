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
from timeit import default_timer as t


def main():
    start = t()
##    print eratosthenes_sieve(10000)
    print rwh_primes1(100)
    stop = t()
    print 'done - took: ' + str(stop - start)


def eratosthenes_sieve(magnitude):
    primes = range(2,magnitude)
    for i in primes:
        multiple = 2*i
        while(multiple < magnitude):
            try:
                 primes.remove(multiple)
            except:
                pass
            finally:
                multiple += i

    return primes

def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


if __name__ == '__main__':
    main()
