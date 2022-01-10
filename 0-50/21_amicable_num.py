import time
import math
def amicable(x):
    res  = []
    for i in range(1,x):
        if (x % i) == 0:
            res.append(i)
    return sum(res)
def main():
    # {1184, 6368, 8128, 6, 5564, 5020, 2924, 28, 496, 284, 6232, 1210, 220, 2620}
    t0 = time.time()
    res = set()
    for i in range(1,10000):
        j = amicable(i)
        if(i == amicable(j) and i != j and amicable(j) != j):
            res.add(i)
            res.add(j)
    print(sum(res))
    t1 = time.time()
    print("time = ",t1-t0)
if __name__ == "__main__":
    main()