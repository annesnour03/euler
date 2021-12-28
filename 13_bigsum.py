def main():
    sum = 0
    for i in open("13_input.txt","r"):
        i = int(i)
        sum += i
    print(int(str(sum)[:10]))

if __name__ == "__main__":
    main()