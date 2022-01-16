import time
import sys
import math as mt

numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]

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

# Generate all possibilities
def master_mutation(res,x,i):
    x = str(x)
    for j in range(i,len(x)):
        formed = str(x)[:j] + "*" + str(x)[j + 1:]
        res.add(formed)
        master_mutation(res,formed,i + 1)
    return res


def solve():
    primes = getprimes(int(1e6))

    for i in range(10000, int(1e6)):
        res = set()
        perm = list(master_mutation(res,i,0))
        pos_res = []
        for j in perm:
            pos_res = []
            for k in numbers:
                c = j.replace('*', str(k))
                if(isprime(int(c)) == False):
                    continue
                if(int(c) in primes and c[0] != '0'):
                    pos_res.append(c)
                else:
                    pos_res = []
                if(len(pos_res) == 8):
                    print(pos_res)
                    return pos_res



def main():
    t0 = time.time()
    ans = solve()
    print(ans[0]) # 500 sec
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
