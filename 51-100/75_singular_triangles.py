from collections import defaultdict
import time
import math
import numpy as np


def answer_present(results, key, answer) -> bool:
    return answer in results[key]


def solve(limit):
    results: dict[int, int] = defaultdict(lambda: 0)

    for m in range(2, (math.isqrt(limit//2)) + 1):
        for n in range(1,  m):
            if (math.gcd(m, n) == 1) and ((n+m) % 2 == 1):
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2

                current = np.array([a, b, c])
                base = current
                k = 1
                while current.sum() <= limit:
                    results[current.sum()] += 1
                    k += 1
                    current = base * k
    combined_results = np.array(list(results.values()))
    return len(combined_results[combined_results == 1])


def main():
    t0 = time.time()
    LIMIT = 1_500_000
    print(solve(LIMIT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
