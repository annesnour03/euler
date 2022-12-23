import time


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


def solve(limit):
    return sum(calc_totient(n) for n in range(limit + 1)) - 1


def main():
    t0: float = time.time()
    LIMIT: int = 10 ** 6
    print(solve(LIMIT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
