import time
import sys
import math


def isprime(x):
    if(x == 2):
        return True
    if(x % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(abs(x))) + 1, 2):
        if x % i == 0:
            return False
    return True


def getprimes(limit):
    res = []
    for i in range(2,limit):
        if(isprime(i)):
            res.append(i)
    return res

primes = getprimes(1000000) # define as a global so we don't have to get new primes each iteration

def getfactors(x):
    # print(primes)
    res = []
    for i in primes[:int(math.sqrt(x)) + 1]:
        while((x % i) == 0):
            x /= i
            res.append(i)
    return res

def solve(streak):
    i = 646
    on_a_roll = 0
    while True:
        factor = getfactors(i)
        if(len(set(factor)) == streak):
            on_a_roll +=1
        else:
            on_a_roll = 0
        if on_a_roll == streak:
            return i - streak + 1
        i +=1


def main():
    t0 = time.time()
    ans = solve(4)
    print(ans)
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
