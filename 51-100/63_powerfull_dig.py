import time
import math

def solve():
    pos = list(range(1,10))
    sol = []
    for power in range(25):
        for i in pos:
            res = i ** power
            size = int(math.log10(res) + 1)
            if size == power:
                sol.append(res)
    return sol

def main():
    t0 = time.time()
    ans = solve()
    print(len(ans))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
