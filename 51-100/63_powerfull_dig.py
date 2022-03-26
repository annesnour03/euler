import time
import sys
import math


def solve():
    print(65 ^ 42)


def main():
    t0 = time.time()
    ans = solve()
    print(ans)
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
