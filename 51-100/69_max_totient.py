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
    calced = 1
    for factor in factors:
        calced *= 1-1/factor
    return 1/calced


def solve(limit):
    maximum = 2
    max_i = None
    for i in range(2, limit):
        value = calc_totient(i)
        if value > maximum:
            maximum = value
            max_i = i

    return max_i


def main():
    t0 = time.time()
    LIMIT = 10 ** 6
    print(solve(LIMIT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
