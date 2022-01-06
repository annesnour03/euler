import time
import sys
import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_pandigital(first, second, third):
    first, second, third = str(first), str(second), str(third)
    combined = first + second + third
    if len(combined) < len(numbers):
        return False
    number = [str(i) for i in numbers]

    if len(set(combined)) != len(combined) or "0" in combined:
        return False
    for i in range(1, len(number) + 1):
        if str(i) not in combined:
            return False
    return True


def solve():
    res = set()
    for i in range(1, 10000):
        for j in range(10000 // i):  # this //i reduces time by 150sec....
            if check_pandigital(i, j, i * j) == True:
                res.add((i * j))
        if i % 1000 == 0:
            print("op de helft", i, j)

    return res


def main():
    t0 = time.time()
    ans = solve()
    print(sorted(ans), sum(ans))

    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
