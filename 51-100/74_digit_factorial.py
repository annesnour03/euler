import time
import functools
import math


def sum_fac_digits(n: int) -> int:
    t: list[int] = list(map(int, list(str(n))))
    return sum(map(math.factorial, t))


def get_chain_len(n: int, master_data) -> int:
    seen: list[int] = []
    current = n
    while current not in seen:
        if current in master_data:
            # Memorize what we have calced.
            total_len = len(seen) + master_data[current]
            master_data[n] = total_len
            return total_len
        else:
            seen.append(current)
            current = sum_fac_digits(current)
    master_data[n] = len(seen)
    return len(seen)


def solve(limit):
    r = 0
    master_data: dict[int, int] = dict()

    chain_length = 60
    for i in range(limit + 1):
        chain = get_chain_len(i, master_data)
        if chain == chain_length:
            r += 1
    return r


def main():
    t0 = time.time()
    LIMIT = 10 ** 6
    print(solve(LIMIT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
