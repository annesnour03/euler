import time

convert = {
    0: "sunday",
    1: "monday",
    2: "tuesday",
    3: "wensday",
    4: "thursday",
    5: "friday",
    6: "saturday",
}
month = {
    1: "january",
    2: "febuary",
    3: "march",
    4: "april",
    5: "may",
    6: "june",
    7: "july",
    8: "august",
    9: "september",
    10: "oktober",
    11: "november",
    12: "december",
}

def main():
    t0 = time.time()
    day = 0
    max = 31
    c = 1
    day_c = 1
    schrikkel = 28
    year = 1901
    sunday_counter = 0
    while True:
        if month.get(c) == "febuary":
            max = schrikkel
        elif month.get(c) == "march":
            max = 31
        elif month.get(c) == "april":
            max = 30
        elif month.get(c) == "may":
            max = 31
        elif month.get(c) == "june":
            max = 30
        elif month.get(c) == "july":
            max = 31
        elif month.get(c) == "august":
            max = 31
        elif month.get(c) == "september":
            max = 30
        elif month.get(c) == "oktober":
            max = 31
        elif month.get(c) == "november":
            max = 30
        elif month.get(c) == "december":
            max = 31
        elif month.get(c) == "january":
            max = 31
        day += 1
        day_c += 1
        if convert.get((day_c % 7)) == "sunday" and day == 1:
            sunday_counter += 1
        if day == max:
            day = 0
            c += 1
            if year % 4 == 0 or year == 2000:
                schrikkel = 29
            else:
                schrikkel = 28
        if c == 13:
            c = 1
            year +=1
        if year > 2000:
            break
    print(sunday_counter,"sunday's")
    t1 = time.time()
    print("time = ", t1 - t0)

if __name__ == "__main__":
    main()
