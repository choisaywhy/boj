import sys

N, K = list(map(int,sys.stdin.readline().split()))
array = [i for i in range(1,N+1)]
answer = []
index = 0
for _ in range(N):
    length = len(array)
    new_index = (index+K-1) % length
    answer.append(array.pop(new_index))
    index = new_index

print("<",end="")
print(*answer,sep=", ",end="")
print(">",end="")



