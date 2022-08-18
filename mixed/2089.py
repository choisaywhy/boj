import sys

N = int(sys.stdin.readline())
answer = ""
while N :
    if N % (-2) < 0 :
        answer += str(N % (-2)+2)
        N = N // (-2) + 1
    else:
        answer += str(N % (-2))
        N //= (-2)
else :
    if not answer :
        answer = "0"
print(answer[::-1]) 