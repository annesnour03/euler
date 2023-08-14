from math import ceil
from scipy.optimize import minimize
import time


def f(pq, limit):
    p, q = pq
    return abs((p * (p - 1) * q * (q - 1)) - 4 * limit)


def solve(limit):
    # Initial guess for p and q
    initial_guess = [25, 55]

    # Perform the minimization
    result = minimize(lambda x: f(x, limit), initial_guess,
                      method='Nelder-Mead')

    # Get the values of p and q that minimize the difference
    p = result.x[0]
    q = result.x[1]

    return ceil((p-1) * (q-1))


def main():
    t0 = time.time()
    LIMIT = 2e6
    print(solve(LIMIT))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
