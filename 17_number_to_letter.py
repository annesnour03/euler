import time

nums_20 = {0 : "",1 : "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven"
        , 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen",
         16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen"}

nums = {-1: "", -2 : "", 20 : "twenty",30 : "thirty", 40 : "forty", 50 : "fifty", 60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety"}

def under_20(i):
    string = (nums_20.get(i))
    return string
def help(i):
    string = ""
    a =  i//10
    b = i % 10
    if(i < 20): return under_20(i)
    string = (nums.get(a * 10))
    string +=(nums_20.get(b))
    return string

def int_to_string(i):
    string = ""
    if(i <  20):
        return under_20(i)
    elif(i < 100):
        a =  i//10
        b = i % 10
        string = (nums.get(a * 10))
        string += (nums_20.get(b))
        return string
    elif(i < 1000):
        a = i//100
        b = i %100
        string = nums_20.get(a) + "hunderd"
        if(b > 0):
            string += "and"
            string += help(b)
        else:
            return string
    else:
        return "onethousand"
    return string

def main():
    t0 = time.time()
    total_len = 0
    for i in range(1,1001):
        print(int_to_string(i))
        total_len += len(int_to_string(i))
    print(total_len)
    t1 = time.time()
    print("time = ",t1-t0)
if __name__ == "__main__":
    main()