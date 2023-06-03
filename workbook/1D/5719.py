
# 1st trial 틀렸습니다
# 여러개의 최단 경로가 같은 노선을 공유하는 경우, 모든 최단 경로를 제외하지 못하는 논리적 오류
import sys
import heapq as hq

def solution(n,m,s,d,roads):
    
    forbidden = [[False]*n for _ in range(n)]
    count_f = 0
    ans = []

    while True:
        routes = [1e10]*n
        routes[s] = 0
        pre = [1e10]*n

        queue = [(routes[s], s)]
        # dijkstra
        while queue:
            dist, node = hq.heappop(queue)

            if routes[node] < dist:
                continue

            for v,p in roads[node]:
                if routes[v] <= dist + p or forbidden[node][v]:
                    continue
                routes[v] = dist + p
                pre[v] = node
                hq.heappush(queue, (routes[v], v))
        
        print(routes)
        print(pre)

        if routes[d] == 1e10 or count_f == m:
            print("-1")
            break

        if ans and ans[-1] < routes[d]:
            print(routes[d])
            break

        ans.append(routes[d])
        
        # forbidden 연산
        nxt = d
        while nxt != s:
            forbidden[pre[nxt]][nxt] = True
            count_f += 1
            nxt = pre[nxt]



if __name__ == "__main__" :
    input = sys.stdin.readline
    
    while True:
        n,m = map(int, input().split())
        
        if (n,m) == (0,0):
            break
        
        s,d = map(int,input().split())
        roads = [[] for _ in range(n)]
        for _ in range(m):
            u,v,p = map(int,input().split())
            roads[u].append((v,p))

        solution(n,m,s,d,roads)