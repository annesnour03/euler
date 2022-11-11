
import time
import math
import random
from typing import Literal


def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2


def get_start_conditions(x) -> tuple[int, Literal[1]]:
    return (math.ceil(math.sqrt(x)), 1)


def get_lowest_solution(m, d, k):
    current: int = abs(m ** 2 - d)
    while True:
        next: int = abs((m + abs(k)) ** 2 - d)
        if next > current:
            return m
        m += abs(k)
        current = abs(m ** 2 - d)

# using Chakravāla


def probe_m(triplet: tuple[int, int, int], d: int):
    a, b, k = triplet
    m = 1
    while True:
        s = a + b*m
        if s % k == 0:
            break
        m += 1
    new_m = get_lowest_solution(m, d, k)
    new_triplet:tuple[int,int,int] = ((new_m * a + d * b)//(abs(k)), (a + b*new_m) //
                   (abs(k)), (new_m**2 - d)//k)
    if k != 1:
        return probe_m(new_triplet, d)
    return triplet


def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def solve(limit) -> dict[int,tuple[int,int]]:
    results: dict[int, tuple[int, int]] = dict()
    for d in range(1, limit + 1):
        if is_square(d):
            continue
        a, b = get_start_conditions(d)
        start_triplet: tuple[int, Literal[1], int] = (a, b, a**2 - d * b ** 2)
        x, y, _ = probe_m(start_triplet, d)
        results[d] = (x, y)

    return results


def main():
    t0 = time.time()
    LIMIT = 1000
    results: dict[int, tuple[int, int]] = solve(LIMIT)
    print(keywithmaxval(results))
    # 0.0338892936706543 s
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
