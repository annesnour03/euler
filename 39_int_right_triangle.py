import time
import sys
import math
from collections import Counter
def solve(p):
    res = []
    for a in range(p):
        print(a)
        for i in range(1,1000):
            if(p <= i):
                continue
            for j in range(1,1000):
                c = math.sqrt(i * i + j * j)
                if (p <= j or p <= j + i or p <= c):
                    continue
                if (i + j + c == a):
                    res.append(a)
    return res

def main():
    t0 = time.time()
    ans = solve(1000)
    print(ans,(Counter(ans))) #193 sec
    print("time = ","\x1b[6;30;42m",time.time() - t0 , "\x1b[0m" )

if __name__ == "__main__":
    main()

