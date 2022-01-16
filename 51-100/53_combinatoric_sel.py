import time
import sys
import math as mt

def calc_com(n,r):
    return mt.factorial(n)//(mt.factorial(r) * (mt.factorial(n-r)))
def solve(max_range):
    c = 0
    for n in range(23,max_range + 1):
        for r in range(1,n):
            if calc_com(n,r) > int(1e6):
                c += 1
    return c


def main():
    t0 = time.time()
    ans = solve(100)
    print(ans) # 0.00653 s
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
