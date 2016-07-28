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
    permutations = []
    digits = [0,1,2,3,4,5,6,7,8,9]
    i = 0
    for x in permute(digits):
        i += 1
        if i == 1000000:
            print x
            break
    stop = t()
    print stop - start

def permute(el):
    if len(el) <= 1:
        yield el
    else:
        for e in el:
            nel = []
            nel.extend(el)
            nel.remove(e)
            for p in permute(nel):
                yield [e] + p






if __name__ == '__main__':
    main()
