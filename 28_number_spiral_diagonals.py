import time
import sys
import math
def solve(size):
    sum = 1
    for i in range(3,size  + 1):
        if i  % 2 != 0:
            sum += 4 * i * i - 6 * i + 6
    return sum

def main():
    t0 = time.time()
    print(solve(1001))
    t1 = time.time()

    print("time = ","\x1b[6;30;42m",t1 - t0 , "\x1b[0m" )


if __name__ == "__main__":
    main()
