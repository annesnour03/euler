import time
import math
import sys
import sympy as sp
sys.setrecursionlimit(5000)

def fraction(x):
    initial=sp.N(sp.sqrt(x), 5000)

    prev_x = initial
    prev_a = math.floor(initial)
    res = [prev_a]
    while len(res) < 500:
        if prev_x - prev_a == 0:
            return []
        x1=1/(prev_x - prev_a)
        a1=int(x1)

        res.append(a1)
        prev_x = x1
        prev_a = a1
    return res
def find_longest_repeat(sequence:list):
    a = '-'.join(str(m) for m in sequence)
    print(a)
    i = (a+"-"+a).find(a, 1, -1)
    return find_longest_repeat(sequence[:-1]) if i == -1 else a[:i]

def solve(limit):
    seq = find_longest_repeat(fraction(13)[1:])
    print(len(seq.split('-')),seq)
    # for i in range(2,14):
        # seq = fraction(i)
        # if seq:
        #     print(seq)


def main():
    t0 = time.time()
    ans = solve(10000)
    print(ans)

    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
