import time
from itertools import permutations
from collections import Counter

def solve(n):
    res = []
    cubes = [i**3 for i in range(10001)]
    strings = list(map(str, cubes))
    for index, i in enumerate(strings):
        strings[index] = ("".join(sorted(i)))
    for (item,key) in Counter(strings).items():
      if key == n:
        res.append(item)

    a =  (int("".join(i)) for i in (permutations(res[0])))
    res.clear()
    for i in a:
      if(iscubic(i)):
        res.append(i)
        return res
    return res

def iscubic(x):
  return round(x ** (1/3)) ** 3 == x

def main():
    t0 = time.time()
    ans = solve(5)
    print( min(ans))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
