import time
import sys
def fact(n):
    if not n: return 1
    return n * fact(n - 1)
def main():
    t0 = time.time()
    ans = list(str(fact(100)))
    ans = [int(i) for i in ans]
    print(sum(ans))
    t1 = time.time()
    print("time = ",t1-t0)
if __name__ == "__main__":
    main()