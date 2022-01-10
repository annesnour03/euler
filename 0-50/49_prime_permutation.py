import time
import sys
import math as mt
import array

def isprime(x):
    if x <= 1:
        return False
    for i in range(2, int(mt.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# Generate permutations
def permutations(s):
    res = set()
    if len(s) <= 1:
        res.add(s)
    else:
        for i in range(len(s)):
            for p in permutations(s[:i] + s[i+1:]):
                res.add(s[i] + p)
    return res

# Checks if given list has a seq that abides given increment
def check_increment(seq,i):
    seq = list(map(int,seq))
    first = 0
    for j in range(len(seq)):
        if seq[j] + i in seq:
            first = seq[seq.index(seq[j] + i)]
            if first + i in seq:
                if seq[j] != 1487 and seq[j] > 1000:
                    return (seq[j],seq[j] + i, + seq[j] + 2*i)
    return 0

def solve():
    seq = []
    for i in range(1000, 9999):
        perm =sorted(permutations(str(i)))
        perm = sorted([j for j in perm if isprime(int(j))])
        if len(perm) >= 3:
            seq.append(perm)

    for i in seq:
        inc = check_increment(i,3330)
        if inc != 0:
            return str(inc[0]) + str(inc[1]) + str(inc[2])
    return 0


def main():
    t0 = time.time()
    ans = solve()
    print(ans) #0.3 sec
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
