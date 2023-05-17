import time


def solve(divisble):

    def p(N):
        dp = [0] * (N + 1)
        dp[0] = 1
        for row in range(1, N + 1):
            if (dp[row] + 1) % divisble == 0:
                return row
            for col in range(row, N + 1):
                if (col >= row):
                    dp[col] = dp[col] + dp[col - row]
                    dp[col] %= divisble
        return dp
    return p(100_000)


def main():
    t0 = time.time()
    DIVISBLE = 1_000_000
    print(solve(DIVISBLE))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
