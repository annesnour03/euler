import time


def solve(limit):
    grid = [0] * (limit + 1)
    grid[0] = 1
    for i in range(1, limit):
        for j in range(i, limit + 1):
            grid[j] += grid[j - i]

    return grid[limit]


def main():
    t0 = time.time()
    LIMIT = 100
    print(solve(LIMIT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
