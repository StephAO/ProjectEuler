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

# success
def main():
    total = 0
    name_file = open("names.txt","r")
    names = []
    names_given = name_file.read().split(',')
    for name in names_given:
        names.append(name.strip('"').lower())
    names.sort()
    print names
    for name in names:
        namescore = 0
        for char in name:
            namescore += (ord(char) - ord('a') + 1)
        total += namescore * (names.index(name) + 1)

    print total




if __name__ == '__main__':
    main()
