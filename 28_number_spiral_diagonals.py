import time
import sys
import math
def solve(size):
    sum =  1
    num = 1
    for i in range(1,2*size):
        sum = num + 2* i
        print(sum)
def main():
    t0 = time.time()
    test = [2,4,6,8,12,16,20,24,30,36,42,48]
    print(solve(5))
    t1 = time.time()

    print("time = ","\x1b[6;30;42m",t1 - t0 , "\x1b[0m" )


if __name__ == "__main__":
    main()
