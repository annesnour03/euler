import time
import math


def paths(i):
    return math.factorial(i + i) // (math.factorial(i) * math.factorial(i))

def main():
    t0 = time.time()
    print(paths(20))

    t1 = time.time()
    print("time = ",t1-t0)
if __name__ == "__main__":
    main()