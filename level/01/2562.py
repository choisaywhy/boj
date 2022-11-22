# list 유지 값만 할당
import sys

input = sys.stdin.readline

maximum = [0,0]

for i in range(9) :
    temp = int(input())
    if temp > maximum[0] :
        maximum[0],maximum[1] = temp, i+1

print(maximum[0], maximum[1], sep="\n")

# list 자체 재할당
import sys

input = sys.stdin.readline

maximum = [0,0]

for i in range(9) :
    temp = int(input())
    if temp > maximum[0] :
        maximum = [temp, i+1]

print(maximum[0], maximum[1], sep="\n")

# 메모리는 같으나, 값만 재할당하는 방법이 시간이 더욱 단축됨