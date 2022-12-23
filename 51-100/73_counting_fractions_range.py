import time
import math


def solve(limit) -> int:
    res = []
    for i in range(1, limit + 1):
        upper_bound = int(i * 1/2)
        for j in range(upper_bound, 1, -1):
            gc: int = math.gcd(i, j)
            if gc != 1:
                continue
            if(j/i < 1/3):
                break
            res.append((j/i, j, i))
    return len(res)


def main():
    t0: float = time.time()
    LIMIT: int = 12_000
    print(solve(LIMIT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
