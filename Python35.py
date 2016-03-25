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
import time

def main():
    stime = time.clock()
    primes = prime_stuff.rwh_primes1(1000000)
    total = 0
    for i,p in enumerate(primes):
##        print(p)
        if i%10000 == 0:
            print(p)
##        print(primes)
        num_digits = math.floor(math.log(p, 10))+1
##        print(p, "Num digits: ", num_digits)
        rotated = set()
        all_prime = True
        r = p
        for d in range(num_digits):
            h = r%10
            r = math.floor(r/10)+math.pow(10,(num_digits-1))*h
            rotated.add(r)
            if not prime_stuff.is_prime(r):
                all_prime = False
                break
            elif r > p:
##                print(primes)
                try:
##                    print(p,r)
                    primes.remove(r)
                except:
                    pass
        if all_prime:
##            print(p, rotated)
            total += len(rotated)
    print(total)
    print(time.clock() - stime)



if __name__ == '__main__':
    main()
