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
month_dict = {
1 : 31,
2 : 28,
3 : 31,
4 : 30,
5 : 31,
6 : 30,
7 : 31,
8 : 31,
9 : 30,
10 : 31,
11 : 30,
12 : 31
}

#success
def main():
    global month_dict
    count = 0
    # date['day'] represents the day of the week, 1 being Monday, 7 being Sunday
    date = {'year' : 1900, 'month' : 1, 'day_num' : 1, 'day' : 1}
    while date['year'] != 2001:
        # check if first day of month is a sunday
        if date['day_num'] == 1 and date['day'] == 7 and date['year'] > 1900:
            count += 1

        # go to next day
        date['day_num'] += 1
        if date['day_num'] > month_dict[date['month']]:
            date['day_num'] = 1
            date['month'] += 1
            if date['month'] == 13:
                date['month'] = 1
                date['year'] += 1
                # check to see if new year is a leap year
                if (date['year'] % 4 == 0 and not date['year'] % 400 == 0):
                    month_dict[2] == 29
                else:
                    month_dict[2] == 28
        date['day'] += 1
        if date['day'] > 7:
            date['day'] = 1
    print count

if __name__ == '__main__':
    main()
