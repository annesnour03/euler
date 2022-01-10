import time
import sys
import math

# Generate permutations
def permutations(s):
    res = []
    if len(s) <= 1:
        res.append(s)
    else:
        for i in range(len(s)):
            for p in permutations(s[:i] + s[i+1:]):
                res.append(s[i] + p)
    return res

def solve():
    primes = [2,3,5,7,11,13,17]
    perm = permutations("9876543210")
    res = []
    for i in perm:
        c = 0
        for j in range(2,9):
            sub = int(i[j - 1: j + 2])
            if(sub % primes[j - 2] == 0):
                c += 1
            else:
                break
        if(c == 7):
            res.append(int(i))
    return res


def main():
    t0 = time.time()
    ans = solve()
    print(ans,sum(ans)) # 6.4 sec
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
