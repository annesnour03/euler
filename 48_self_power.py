import time
import sys
import math

def solve(limit,cutoff):
    a = lambda x :x**x
    return (str(sum([a(i)for i in range(1, limit + 1)])))[-cutoff:]

def main():
    t0 = time.time()
    ans = solve(1000,10)
    print(ans)
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
