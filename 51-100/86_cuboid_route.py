import time
import math
from tqdm import tqdm


def is_integer_shortest_path(x, y, z):
    n = x * x + (y + z) * (y + z)
    s = math.isqrt(n)
    return s * s == n


def is_running_sum_greater_than_limit(limit_to_num_solutions, limit):
    return sum(limit_to_num_solutions.values()) >= limit

def solve(limit):
    s = 0
    with tqdm(total=limit, desc="Solutions", unit="") as pbar:
        for x in range(1, limit + 1):
            for y in range(1, x + 1):
                for z in range(1, y + 1):
                    if is_integer_shortest_path(x, y, z):
                        s += 1
                        pbar.update(1)
                    if s >= limit:
                        return max(x, y, z)


def main():
    t0 = time.time()
    LIMIT = 1_000_000
    print(solve(LIMIT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
