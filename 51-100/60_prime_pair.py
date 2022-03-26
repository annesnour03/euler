import time
import sys
import math


def solve(x):
    return (((list(str(x)))[::-1])) == list(str(x))


def main():
    t0 = time.time()
    ans = solve(112)
    print(ans)
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
