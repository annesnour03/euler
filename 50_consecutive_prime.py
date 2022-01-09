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
    res = [2]
    for i in range(1,limit,2):
        if(isprime(i)):
            res.append(i)
    return res

def solve(limit):
    primes = getprimes(limit)
    res = {}
    for a in primes[::-1]:
        print(a)
        for i in range(int(mt.sqrt(a)) + 1):
            for j in range(int(mt.sqrt(a)) + 1,i,-1):
                temp_sump = sum(primes[i:j])
                if(list(res.keys()).count(a) == 0 and temp_sump == a):
                        res[a] = len(primes[i:j])
    return res

def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]
    
def main():
    t0 = time.time()
    ans = solve(1000)
    print(keywithmaxval(ans))
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
