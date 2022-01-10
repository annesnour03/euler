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

# Only get primes that in total sum up below given limit
def getprimes(limit):
    res = [2]
    total = 0
    for i in range(1, limit, 2):
        if(isprime(i)):
            res.append(i)
            total += i
        if (total > limit):
            return res
    return res


def solve(limit):
    primes = getprimes(limit)
    res = []
    l2 = 0
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            cut_primes = primes[i:j]
            temp_sump = sum(cut_primes)
            l = len(cut_primes)

            if(l >= l2 and isprime(temp_sump)):
                res.append(temp_sump)
                l2 = l
    return res[-1]


def main():
    t0 = time.time()
    ans = solve(int(1e6))  # 0.14 sec
    print(ans)
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
