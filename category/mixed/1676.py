import sys
from math import factorial


N = int(sys.stdin.readline())

fac = factorial(N)
count = 0

while True :
    if not fac % 10 :
        count += 1
        fac //= 10
    else :
        break
print(count)