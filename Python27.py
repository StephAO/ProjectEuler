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
import prime_stuff
import time

def main():
    stime = time.clock()
    topj = 0
    product = 0
    primes = [1]
    primes.extend(prime_stuff.rwh_primes1(2001000))
    puot = [p for p in primes if p < 1000]
    for i, a in enumerate(reversed(puot)):
        for b in reversed(puot):
            if b < a:
                break
            broken = [False,False,False,False]
            for j in range(b):
                if not broken[0] and not prime_stuff.is_prime(j**2 + j*a + b):
                    broken[0] = True
                if not broken[1] and not prime_stuff.is_prime(j**2 - j*a + b):
                    broken[1] = True
                if not broken[2] and not prime_stuff.is_prime(j**2 + j*a - b):
                    broken[2] = True
                if not broken[3] and not prime_stuff.is_prime(j**2 - j*a - b):
                    broken[3] = True
                if all(broken):
                    break
                if j > topj:
                    topj = j
                    print(broken)
                    product = a*b if broken[1] and broken[2] else a*b*(-1)

        if topj > a:
            break
    print(product)
    print(time.clock() - stime)






if __name__ == '__main__':
    main()
