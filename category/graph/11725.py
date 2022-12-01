import sys
from collections import deque
sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def traversal(tree,node,visited,answer) :

    visited[node] = True

    for next in tree[node] :
        if visited[next]: 
            continue
        answer[next] = node
        traversal(tree,next,visited,answer)
    return answer

N = int(input())
tree = {}
answer = [0] * (N+1)

for _ in range(N-1):
    x, y = list(map(int, input().split()))
    tree[x] = tree.get(x,[])+[y]
    tree[y] = tree.get(y,[])+[x]

answer = traversal(tree,1,[False] * (N+1),answer)

for i in range(2,N+1):
    print(answer[i])

# 
# def function ( a = []): 로 선언할 때, a는 한 곳에 할당되므로, 
# function을 새로 호출해도 이전에 사용한 a 기록이 남아있음