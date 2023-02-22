# bfs + kruskal로 풀기 요망
# 자세한 사항 노트


import sys
from collections import deque

def solution(N,M,maps):
    
    def BFS(start) :
        queue = deque([start])
        visited = []

        while queue :
            x, y = queue.popleft()
            







if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    maps = []
    for i in range(N) :
        maps.append(list(map(int, input().split())))
    
    solution(N,M,maps)