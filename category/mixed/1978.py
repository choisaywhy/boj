import sys
from math import sqrt

def primary(num:int)->bool:
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            return False
    return True


N = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
count = 0
for num in array :
    if primary(num):
        count += 1

print(count)
