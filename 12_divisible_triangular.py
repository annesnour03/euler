import math
import sys
import time

def tnumber(x):
    return (int((x**2 + x) // 2))

def num_div(x):
    x = int(x)
    counter = 0
    for i in range(1,int(math.sqrt(x)) + 1):
        if(x % i) == 0:
            counter +=2
    return counter

def main():
    t0 = time.time()
    for i in range(sys.maxsize):
        if(num_div(tnumber(i)) > 500):
            print(tnumber(i))
            break
    t1 =time.time()
    print("time taken ",t1-t0)
if __name__ == "__main__":
    main()