import sys
from collections import deque

def solution(N, M) :
    graph = {}
    singer = [0] * (N+1)

    for _ in range(M) :
        temp = list(map(int, input().split()))
        for i in range(1, temp[0]) :
            graph[temp[i]] = graph.get(temp[i],[]) + [temp[i+1]]
            singer[temp[i+1]] += 1

    queue = deque()
    ans = []

    for i in range(1, N+1) :
        if singer[i] == 0 :
            queue.append(i)
    
    while queue :
        node = queue.popleft()
        ans.append(node)
     
        for i in graph.get(node,[]) :
            singer[i] -= 1
            
            if singer[i] == 0:
                queue.append(i)
    
    if len(ans) != N :
        print(0)
    else :
        for a in ans :
            print(a)



if __name__ == "__main__" :
    N, M = map(int, input().split())
    solution(N,M)