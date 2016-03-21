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

#success
def main():
    grid = [[0 for x in range(21)] for x in range(21)]
    for i in range(0,21):
        for j in range(0,21):
            if i == 0 and j == 0:
                grid[i][j] = 1
            else:
                above = 0
                leftwards = 0
                if j-1 >= 0:
                    above = grid[i][j-1]
                if i-1 >= 0:
                    leftwards = grid[i-1][j]
                grid[i][j] = above + leftwards
    print grid[20][20]

if __name__ == '__main__':
    main()
