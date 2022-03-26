import time
import sys
import math

# need 9 bits
def solve(input):
        for i in range(97,123):
            for j in range(97,123):
                for k in range(97,123):
                    for num in input:
                        total = i + j + k
                        encry = chr(total ^ ord(num))
                        if(encry ^ total == num):
                            # print(chr(encry),end="")
                            print(num)
                print("")



def main():
    t0 = time.time()
    file = list(open('59_input.txt','r').readline().split(','))
    file = [chr(int(i)) for i in file]
    print(file) 
    ans = solve(file)
    print(ans)
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
