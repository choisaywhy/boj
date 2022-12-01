import sys

N, B = map(int, sys.stdin.readline().split())

answer =""
while N :
    if N % B >= 10 :
        answer += chr(ord('A') + (N % B) - 10)
    else :
        answer += str(N % B)
    N //= B

print(answer[::-1])