import time
import math
import sys
import sympy as sp
sys.setrecursionlimit(5000)

def fraction(x):
    initial=sp.N(sp.sqrt(x), 2000)

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
    split_out = '-'.join(str(m) for m in sequence)
    while True:
        i = (split_out+"-"+split_out).find(split_out, 1, -1)
        if i == -1:
            # Remove all after last "-"
            split_out = "-".join(split_out.split("-")[:-1])
        else:
            return split_out[:i]

def solve(limit):
    res = []
    for i in range(2,limit + 1):
        if sp.sqrt(i).is_integer:
            continue
        seq = find_longest_repeat(fraction(i)[1:]).split('-')
        # Filter emptys
        seq = [x for  x in seq if x]
        res.append((seq))
    return len([*filter(lambda x: len(x) %2 ,res)])
def main():
    t0 = time.time()
    ans = solve(10000)
    print(ans)
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
