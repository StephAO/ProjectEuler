
def min(a,b):
    return a if a < b else b

results = {}
def numb_comb(numberOfBalls, maxGroupSize):

    result = results.get((numberOfBalls, maxGroupSize))
    if result != None:
        return result
    else:
        result = 1

    for i in xrange(2, min(numberOfBalls, maxGroupSize)+1):
        result += numb_comb(numberOfBalls - i, i)

    results[(numberOfBalls, maxGroupSize)] = result
    return result

def main():
    print "?"
    i = 1
    while True:
        i += 1
        nc = numb_comb(i,i)
        print i, "=>", nc
        if nc%1000000 == 0:
            print "Solution: ", i
            break


if __name__ == "__main__":
  main()
