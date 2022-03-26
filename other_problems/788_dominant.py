import time
import sys
import math
from typing import Counter

# 20221
def is_dominating(x):
    occurence = [0 for _ in range(10)]
    for index, i in enumerate(list(str(x))):
        occurence[int(i)] +=1
    filtered = list(filter(lambda occ:occ > len(str(x)) //2, occurence))
    if(filtered):
        return True
# 6 --> 10^7 == 27280 (10 + 9x3030)
# 5 --> 10^6 == 1270 (10 + 9x140)
# 4 --> 10^5 == 856 (10 + 9x94)
# 3 --> 10^4 == 37 (10 + 9x3)
# 2 --> 10^3 == 28 (10 + 9x2)
# 1 --> 10^2 == 9
def solve(limit):
    return ([i for i in range(10**2,limit) if is_dominating(i)])
    exit()


def main():
    t0 = time.time()
    ans = solve(10**3)
    print(ans)
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
