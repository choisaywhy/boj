import sys

N= str(sys.stdin.readline()).strip()
answer = ""
count = 0
temp = 0
N = N[::-1]
for i in range(len(N)):
    temp += int(N[i]) * (2**count)
    count += 1
    
    if count == 3:
        answer += str(temp)
        temp = 0
        count = 0
    elif i == len(N) - 1:
        answer += str(temp)

print(answer[::-1])