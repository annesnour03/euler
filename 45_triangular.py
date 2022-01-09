import time
import sys
import math


def pentagonal(limit):
    for i in range(1, limit + 1):
        yield(int(0.5 * (3 * i * i - i)))


def triangle(limit):
    for i in range(1, limit):
        yield(int(0.5 * i * i + 0.5*i))


def hexagonal(limit):
    for i in range(1, limit):
        yield(int(i * (2 * i - 1)))


def unify(x, y, z):
    return list(set(x) & set(y) & set(z))[-1]


def solve(limit):
    final = unify(list(pentagonal(limit)), list(
        triangle(limit)), list(hexagonal(limit)))
    return final


def main():
    t0 = time.time()
    ans = solve(100000) # 0.06 sec
    print(ans)
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
