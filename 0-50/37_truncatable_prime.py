from tabnanny import check
import time
import sys
import math


def isprime(x):
    """Checks if a given number is a prime."""
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def cut(x, side):
    """Cuts a piece off of a number depending on which side is specified."""
    if x < 10:
        return x
    if side == "last":
        return x//10
    if side == "first":
        return int(str(x)[1:])


def check_general(x, side):
    """Checks if a number is a truncatable prime."""
    length = int(math.log10(x)) + 1
    for _ in range(length):
        if(isprime(x) == False):
            return False
        x = cut(x, side)
    return True


def check_truncatable(x):
    return check_general(x, "last") and check_general(x, "first")


def solve(limit):
    res = []
    for i in range(8, limit):
        if(check_truncatable(i)):
            res.append(i)
    return res


def main():
    t0 = time.time()
    ans = solve(1000000)
    print(ans, sum(ans))

    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
