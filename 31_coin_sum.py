import time
import sys
import math
def coinChange(S, sum):

    if sum == 0:
        return 0

    if sum < 0:
        return sys.maxsize

    coins = sys.maxsize

    for c in S:

        result = coinChange(S, sum - c)

        if result != sys.maxsize:
            coins = min(coins, result + 1)

    return coins
def main():
    t0 = time.time()
    # coins = [1,2,5,10,20,50,100,200]
    coins = [1,2,5,10]
    print(coinChange(coins,10))
    t1 = time.time()

    print("time = ","\x1b[6;30;42m",t1 - t0 , "\x1b[0m" )


if __name__ == "__main__":
    main()
