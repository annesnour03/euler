import time
import sys
import math

def solve(max_range):
    ans = set()
    for i in range(2,max_range + 1):
        for j in range(2,max_range + 1):
            ans.add(i ** j)
    return sorted(ans)
def main():
    t0 = time.time()
    max_range = 100
    ans = solve(max_range)
    print(len(ans))
    t1 = time.time()

    print("time = ","\x1b[6;30;42m",t1 - t0 , "\x1b[0m" )

if __name__ == "__main__":
    main()
