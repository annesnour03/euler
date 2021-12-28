import time
import itertools

def permutation(num,ith):
    l = list(itertools.permutations(num))
    return (sorted(l)[ith])
def main():
    t0 = time.time()
    input = [0,1,2,3,4,5,6,7,8,9]
    print(permutation(input,999999))
    t1 = time.time()
    print("time = ",t1-t0)

if __name__ == "__main__":
    main()