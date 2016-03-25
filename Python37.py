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
import prime_stuff
import math
def main():
##    print(truncatable(3797))
    found = []
    primes = prime_stuff.rwh_primes1(1000000)
    primes.remove(2)
    primes.remove(3)
    primes.remove(5)
    primes.remove(7)
    for p in primes:
        if truncatable(p):
            print(p)
            found.append(p)
            if len(found) >= 11:
                break
    print(sum(found))

def truncatable(n):
    num_digits = math.floor(math.log(n,10))
    l = n
    r = n
    for i in range(num_digits):
        r = math.floor(r/10)
        l = l%(math.pow(10,num_digits-i))
##        print(l,r)
        if not prime_stuff.is_prime(l) or not prime_stuff.is_prime(r):
            return False
    return True


if __name__ == '__main__':
    main()
