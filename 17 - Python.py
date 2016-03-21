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

number_dict = {
1 : 'one',
2 : 'two',
3 : 'three',
4 : 'four',
5 : 'five',
6 : 'six',
7 : 'seven',
8 : 'eight',
9 : 'nine',
10 : 'ten',
11 : 'eleven',
12 : 'twelve',
13 : 'thirteen',
14 : 'fourteen',
15 : 'fifteen',
16 : 'sixteen',
17 : 'seventeen',
18 : 'eighteen',
19 : 'nineteen',
20 : 'twenty',
30 : 'thirty',
40 : 'forty',
50 : 'fifty',
60 : 'sixty',
70 : 'seventy',
80 : 'eighty',
90 : 'ninety',
1000: 'onethousand',
}

#success
def main():
    num_l = 0
    for i in range(1,1001):
        if i == 1000:
            num_l += len(number_dict[i])
        else:
            # number of hundreds
            h = i//100
            if h > 0:
                num_l += len(number_dict[h]) + len('hundred')
            #initial number of tens
            t = i - (h*100)
            if h > 0 and t > 0:
                    num_l +=  len('and')
            if t < 20 and t > 0:
                num_l += len(number_dict[t])
            else:
                # number of ones
                o = t % 10
                # round number of tens down
                t -= o
                if t > 0:
                    num_l += len(number_dict[t])
                if o > 0:
                    num_l += len(number_dict[o])

    print num_l



if __name__ == '__main__':
    main()
