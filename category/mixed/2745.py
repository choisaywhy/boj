import sys

N, B = map(str, sys.stdin.readline().split())
B = int(B)
answer = 0
for i in range(len(N)):
    num = 0
    if ord(N[i]) >= ord('A') and ord(N[i]) <= ord('Z') :
        num = ord(N[i]) - ord('A') + 10
    else :
        num = int(N[i])

    if i < len(N) - 1:
        answer = (answer+num)*B
    else :
        answer += num

print(answer)