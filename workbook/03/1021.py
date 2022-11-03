import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
queue = deque([i for i in range(1,N+1)]) # front 첫번째 원소 없어짐
answer = 0

for target in list(map(int, input().split())) :
    if queue[0] != target :
        next = queue.index(target)
        if next > len(queue) // 2 :
            while queue[0] != target :
                queue.appendleft(queue.pop())
                answer += 1
        else :
            while queue[0] != target :
                queue.append(queue.popleft())
                answer += 1

    queue.popleft()

print(answer)