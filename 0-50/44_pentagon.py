import time
import math

# Generates pentagonal numbers
def pentagonal(limit):
    for i in range(1, limit + 1):
        yield(int(0.5 * (3 * i * i - i)))

# The inverse of the pentagonal function, this function redcues time from 45s --> 0.46sec
def ispentagonal(x):
    inverse = (1/6) * (1 + math.sqrt(24 * x + 1))
    return inverse.is_integer()


def solve(limit):
    pent = list(pentagonal(limit))
    for i in range(1, limit):
        for j in range(i, limit):
            if (ispentagonal(pent[i] + pent[j]) and ispentagonal(abs(pent[i] - pent[j]))):
                return abs(pent[i] - pent[j])


def main():
    t0=time.time()
    ans=solve(2500)  # 0.46sec
    print(ans)
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")

if __name__ == "__main__":
    main()
