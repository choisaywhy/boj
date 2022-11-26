import sys
from collections import deque

input = sys.stdin.readline

def DFS(N, start) :
    stack = deque([start])
    visited = [False for _ in range(N)]

    while stack :
        node = stack.pop()
        if not visited[node] :
            print(node, sep=" ")
            visited[node] = True
            for i in range(N) :
                if visited[i] :
                    continue
                stack.append(i)
    return stack               
    


N, M = map(int, input().split())

for i in range(N) :
    DFS(N, i)
    print()
#     print(DFS(N, i))