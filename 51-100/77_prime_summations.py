import time
import math as mt
import numpy as np


def isprime(x):
    if x <= 1:
        return False
    for i in range(2, int(mt.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def getprimes(limit):
    res = [2]
    for i in range(1, limit, 2):
        if isprime(i):
            res.append(i)
    return res


def solve(limit):
    grid = np.array([0] * (limit + 1))
    grid[0] = 1
    primes = getprimes(5000)
    for prime in primes:
        for i in range(0, limit - prime + 1):
            grid[prime + i] += grid[i]
    return np.argmax(grid > 5000)


def main():
    t0 = time.time()
    LIMIT = 1000
    print(solve(LIMIT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
