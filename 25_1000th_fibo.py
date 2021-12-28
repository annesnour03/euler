import time
import sys
import math

def main():
    t0 = time.time()
    digits = 1000
    arr = [1,1]
    i = len(arr)

    while math.log10(arr[-1]) + 1 <= digits:
        arr.append(arr[i - 1] + arr[i - 2])
        i += 1
    print(i)
    t1 = time.time()
    print("time = ", t1 - t0)


if __name__ == "__main__":
    main()
