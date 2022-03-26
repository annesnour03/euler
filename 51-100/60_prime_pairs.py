from subprocess import check_output
from tabnanny import check
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
    for i in range(1, limit, 2):
        if(isprime(i)):
            res.append(i)
    return res
primes = getprimes(10000)
def solve():
    res = {}
    for i in primes:
        for j in primes:
            if(not checkconcat(i,j)):
                continue
            for k in primes:
                if(not checkconcat(k,j) or not checkconcat(k,i)):
                    continue
                for l in primes:
                    if(not checkconcat(l,k) or not checkconcat(l,j) or not checkconcat(l,i)):
                        continue
                    for m in primes:
                        if(not checkconcat(m,l) or not checkconcat(m,k) or not checkconcat(m,j) or not checkconcat(m,i)):
                            continue
                        res[i+j+k+l+m] = (i,j,k,l,m)
                        print(i,j,k,l,m)
    return res

def checkconcat(x,y):
    return isprime(int(str(x) + str(y))) and isprime(int(str(y) + str(x)))

def main():
    t0 = time.time()
    ans = solve()
    print(ans)
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
