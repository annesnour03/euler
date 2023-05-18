import time
import math
from decimal import *


def solve(limit):
    getcontext().prec = 102
    def digital_sum(x): return sum(
        [int(i) if i.isnumeric() else 0 for i in str(x)])

    def is_rational(x): return x == int(x)
    irrationals = [i for i in range(
        limit) if not is_rational(math.sqrt(i))]
    total = 0
    for i in irrationals:
        a = Decimal(str(i))
        total += digital_sum(str(a.sqrt())[:101])
        print(total, str(a.sqrt()), i)
    return total


def main():
    t0 = time.time()
    LIMIT = 100
    print(solve(LIMIT, LIMIT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
