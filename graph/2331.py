import sys

input = sys.stdin.readline

A,P = map(int,input().split())
arr = [A]
answer = 0

while True :
    num = str(arr[-1])
    next = 0
    for n in num :
        next += int(n)**P
    if next in arr :
        answer = arr.index(next) 
        break
    arr.append(next)

print(answer)
    



