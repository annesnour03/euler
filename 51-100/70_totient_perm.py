import time
from collections import Counter


def prime_factors(n: int):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def totient_factors(n):
    return list(set(prime_factors(n)))


def calc_totient(n):
    factors = totient_factors(n)
    calced = n
    for factor in factors:
        calced *= 1-1/factor
    return int(calced)


def is_permutation(x: int, y: int):
    return Counter(str(x)) == Counter(str(y))


def solve(limit):
    maximum = 999999
    max_i = None
    for i in range(2, limit):
        value = calc_totient(i)
        if i/value < maximum and is_permutation(value, i):
            maximum = i/value
            max_i = i
            print(i, value, maximum)

    return max_i


def main():
    t0 = time.time()
    LIMIT = 10 ** 7
    print(solve(LIMIT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
