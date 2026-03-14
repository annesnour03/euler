import math
import time
from pprint import pprint

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

def solve(limit):
    r = set()
    primes = getprimes(math.isqrt(limit) + 1)
    p2 = [p*p for p in primes if p*p < limit]
    p3 = [p*p*p for p in primes if p*p*p < limit]
    p4 = [p*p*p*p for p in primes if p*p*p*p < limit]
    for c2 in p2:
        for c3 in p3:
            if c2 + c3 > limit:
                break
            for c4 in p4:
                if c2 + c3 + c4 > limit:
                    break
                r.add((c2 + c3 + c4))
    return len(r)
def main():
    t0 = time.time()
    LIMIT = 50_000_000
    ans = solve(LIMIT)
    pprint(ans)
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
