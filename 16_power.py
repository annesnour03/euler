import time
import math
import itertools
import operator


def sum_power(i):
    i = list(map(int,str(int(math.pow(2,i)))))
    res = itertools.accumulate(i,operator.add)
    print(list(res)[-1])

def main():
    t0 = time.time()
    sum_power(1000)
    t1 = time.time()
    print("time = ",t1-t0)
    
if __name__ == "__main__":
    main()