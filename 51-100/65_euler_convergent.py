import time
import math
import sympy as sp
from fractions import Fraction
import sys
sys.setrecursionlimit(5000)

def fraction(x):
    initial = sp.N(x, 20000)
    prev_x = initial
    prev_a = math.floor(initial)
    res = [prev_a]
    while len(res) < 900:
        if prev_x - prev_a == 0:
            return []
        x1 = 1/(prev_x - prev_a)
        a1 = int(x1)

        res.append(a1)
        prev_x = x1
        prev_a = a1
    return res

def get_convergent(number):
    if not number:
        return 0
    if len(number) ==1:
        return Fraction(number[0])
    return Fraction(number[0]) + Fraction(1,get_convergent(number[1:]) )
def solve(number):
    # return (get_convergent(number).numerator)
    return sum ([int(i) for i in str(get_convergent(number).numerator)])

def main():
    t0 = time.time()
    NUMBER_CONVERGENT = 100
    e=2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424371075390777449920695517027618386062613313845830007520449338265602976067371132007093287091274437470472306969772093101416928368190255151086574637721112523897844250569536967707854499699679468644549059879316368892300987931277361782154249992295763514822082698951936680331825288693984964651058209392398294887933203625094431173012381970684161403970198376793206832823764648042953118023287825098194558153017567173613320698112509961818815930416903515988885193458072738667385894228792284998920868058257492796104841984443634632449684875
    # ans=solve(fraction(e)[:NUMBER_CONVERGENT])
    # print(ans)
    print(get_convergent(fraction(e)[:21]))
    print(get_convergent(fraction(e)[:20]))
    print(fraction(e)[:21])
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
