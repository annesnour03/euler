import time
import math

def solve(limit):
    m, n, c = 1, 1, 0
    for i in range(limit):
        n, m = n+m, m + 2 * n
        if(int(math.log10(m)) > int(math.log10(n))):
            c += 1
    return c


def main():
    t0 = time.time()
    ans = solve(1000)
    print(ans)  # 0.0005 s
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
