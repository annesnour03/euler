import time
import sys
import math
def solve(size):
    current =  1
    maal = 2
    c = 1
    res = [1]
    # 1,3,5,7,13,17,21,25
    for i in range(2*size):
        if c % 5 == 0:
            maal += 2
        current = current + maal
        res.append(current)
        c += 1
        print(res)
    print(sum(res))

def main():
    t0 = time.time()
    test = [2,4,6,8,12,16,20,24,30,36,42,48]
    print(solve(7))
    print([1,3,5,7,9,13,17,21,25,31,37,43,49])
    t1 = time.time()

    print("time = ","\x1b[6;30;42m",t1 - t0 , "\x1b[0m" )


if __name__ == "__main__":
    main()
