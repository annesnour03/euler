import time
from pprint import pprint
from functools import cache


def prime_factors(n: int) -> list[int]:
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


@cache
def factor_combinations(n: int):
    primes = prime_factors(n)

    def backtrack(start, current):
        if start == len(primes):
            result.add(tuple(sorted(current)))
            return

        for i in range(len(current)):
            # Try multiplying into existing group
            new_current = current.copy()
            new_current[i] *= primes[start]
            backtrack(start + 1, new_current)

        # Or start a new group
        backtrack(start + 1, current + [primes[start]])

    result = set()
    backtrack(0, [])
    
    return [ list(r) for r in result]


def get_minimal_product_sum(k):
    starting_sum_side = k 
    upper_bound = k * 2

    for n in range(starting_sum_side, upper_bound + 1):
        factors = factor_combinations(n)
        for factor in factors:
            len_factors = len(factor)
            remaining = k - len_factors
            if sum(factor) + remaining == n:
                return (n, (factor, remaining))

    pass


def solve(limit):
    spots = []
    for k in range(2,limit + 1):
        print(k)
        ans = get_minimal_product_sum(k)
        spots.append(ans)
    unique_ns = set([i[0] for i in spots if i is not None])
    return sum(unique_ns)

def main():
    t0 = time.time()
    LIMIT = 12000
    ans = solve(LIMIT)
    pprint(ans)
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
print('testing')