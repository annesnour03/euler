import time
import sys
import math


def isprime(x):
    if  x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def cut(x, dir):
    if x < 10:
        return x
    x = list(str(x))
    x.pop(dir)
    x = int("".join(x))
    return x


def checkl(x):
    length = int(math.log10(x)) + 1
    for i in range(length):
        if(isprime(x) == False):
            return False
        x = cut(x,0)
    return True

def checkr(x):
    length = int(math.log10(x)) + 1
    for i in range(length):
        if(isprime(x) == False):
            return False
        x = cut(x,-1)
    return True

def solve():
    res = []
    for i in range(8, 1000000):
        if(checkl(i) and checkr(i)):
            res.append(i)
    return res


def main():
    t0 = time.time()
    ans = solve()
    print(ans,sum(ans))

    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
