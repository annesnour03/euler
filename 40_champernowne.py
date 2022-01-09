import time
import sys
import math
def irrational():
    com =  ""
    for i in range(0, 1000000 + 1):
        com += str(i)
    return com

def nth(string):
    i = 1
    expr = 1
    while i <= 1000000:
        expr *= int(string[i])
        i *=10
    return expr
def main():
    t0 = time.time()
    print(nth(irrational()))
    print("time = ","\x1b[6;30;42m",time.time() - t0 , "\x1b[0m" )

if __name__ == "__main__":
    main()

