import time
from fractions import Fraction


def continued_fraction_coefficients(x) -> list[int]:
    seq = [2 * (i+1) // 3 if i % 3 == 2 else 1 for i in range(x)]
    seq[0] += 1
    return seq


def get_convergent(number) -> Fraction | int:
    if not number:
        return 0
    if len(number) == 1:
        return Fraction(number[0])
    return Fraction(number[0]) + Fraction(1, get_convergent(number[1:]))


def solve(limit) -> int:
    frac: Fraction | int = get_convergent(continued_fraction_coefficients(limit))
    return sum(list(map(int, (str(frac.numerator)))))


def main():
    t0 = time.time()
    NUMBER_CONVERGENT = 100
    print(solve(NUMBER_CONVERGENT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
