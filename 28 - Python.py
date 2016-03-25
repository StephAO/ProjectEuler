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

def main():
    total = 1
    previous = 1
    for i in range(2,1001,2):
        for j in range(4):
            print(j,previous)
            previous += i
            total += previous
    print(total)

if __name__ == '__main__':
    main()
