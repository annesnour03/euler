import time
import sys
import math as mt


def isprime(x):
    if x <= 1:
        return False
    for i in range(2, int(mt.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def getprimes(limit):
    res = []
    for i in range(limit):
        if(isprime(i)):
            res.append(i)
    return res

def solve(limit):
    i = 3
    primes = getprimes(limit)
    while True:
        c = 0
        for k in range(int(mt.sqrt(i//2)) + 1):
            if(i - 2 *k *k in primes):
                break
            else:
                c +=1
        if c == int(mt.sqrt(i//2))+  1:
            return i
        i += 2


def main():
    t0 = time.time()
    ans = solve(10000)
    print(ans) # 0.09 sec
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
