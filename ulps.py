import sys
import math

def get_exponent(value, base):
    exp = 0
    while value >= base:
        value /= base
        exp += 1

    return exp

def ulps(x, y) -> float:
    if x*y < 0 or x == 0 or y == 0 or math.isinf(x) or math.isinf(y):
        return float('inf')
    
    base = sys.float_info.radix
    epsilon = sys.float_info.epsilon
    
    #print(x)
    #print(y)
    x = abs(x)
    y = abs(y)

    exp_x = get_exponent(x, base)

    exp_y = get_exponent(y, base)

    #print(exp_x)
    #print(exp_y)

    if exp_x == exp_y:
        print("exponents are the same")
        return abs(x - y) / (epsilon * base**exp_x)
    elif abs(exp_x - exp_y) == 1:
        print("exponents differ by one")
        intervalsFromSmaller = (base**(min(exp_x, exp_y) + 1) - min(x, y)) / (epsilon * base**min(exp_x, exp_y))
        intervalsToLarger = (max(x, y) - (base**max(exp_x, exp_y))) / epsilon
        return intervalsFromSmaller + intervalsToLarger
    else:
        print("exponents differ by more than one\nexp_x: ", exp_x, "\nexp_y: ", exp_y)
        intervalsFromSmaller = (base**(min(exp_x, exp_y) + 1) - min(x, y)) / (epsilon * base**min(exp_x, exp_y))
        intervalsToLarger = (max(x, y) - (base**max(exp_x, exp_y))) / (epsilon * base**max(exp_x, exp_y))
        partBIntervals = intervalsFromSmaller + intervalsToLarger
        rangeOfExp = (max(exp_x, exp_y) - min(exp_x, exp_y)) - 1
        intervalsInRange = rangeOfExp * (base / (epsilon * base**rangeOfExp))
        return partBIntervals + intervalsInRange
    
if __name__ == '__main__':
    print(ulps(-1.0, -1.0000000000000003)) #1
    print(ulps(1.0, 1.0000000000000003)) #1
    print(ulps(1.0, 1.0000000000000004)) #2
    print(ulps(1.0, 1.0000000000000005)) #2
    print(ulps(1.0, 1.0000000000000006)) #3
    print(ulps(0.9999999999999999, 1.0)) #1
    print(ulps(0.4999999999999995, 2.0)) #9007199254741001
    print(ulps(0.5000000000000005, 2.0)) #9007199254740987
    print(ulps(0.5, 2.0)) #9007199254740992
    print(ulps(1.0, 2.0)) #4503599627370496
    print(2.0**52) #4503599627370496.0
    print(ulps(-1.0, 1.0)) #inf
    print(ulps(-1.0, 0.0)) #inf
    print(ulps(0.0, 1.0)) #inf
    print(ulps(5.0, math.inf)) #inf
    print(ulps(15.0, 100.0)) #12103423998558208