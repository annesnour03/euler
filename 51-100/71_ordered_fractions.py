import time
import math


def solve(limit) -> int:
    smallest = (0, 0, 0)
    POINT: float = 3/7
    for i in range(1, limit + 1):
        j: int = int(i * 3/7)
        gc: int = math.gcd(i, j)
        if gc != 1:
            continue
        if(j/i < POINT and j/i > smallest[0]):
            smallest: tuple[float, int, int] = (j/i, j, i)
    return smallest[1]


def main():
    t0: float = time.time()
    LIMIT: int = 10 ** 6
    print(solve(LIMIT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
