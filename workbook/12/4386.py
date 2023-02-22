import sys
import heapq

def solution(n, stars):
    parents = [i for i in range(n)]
    graph = []
    ans = 0

    def dist(star1, star2) :
        x1, y1 = star1
        x2, y2 = star2
        return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)


    def find(star) :
        if parents[star] != star :
            parents[star] = find(parents[star])
        return parents[star]
    
    def union(star1, star2) :
        p1 = find(star1)
        p2 = find(star2)

        parents[max(p1, p2)] = min(p1, p2)

    for i in range(n-1) :
        for j in range(i+1,n) :
            heapq.heappush(graph, (dist(stars[i], stars[j]), i, j))
    
    while graph :
        cost, x, y = heapq.heappop(graph)

        if find(x) == find(y) :
            continue
        else :
            union(x, y)
            ans += cost


    print(f"{ans:.2f}")





if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    stars = [tuple(map(float, input().split())) for _ in range(n)]
    solution(n, stars)



# (0,0) 원점을 기준으로 거리 계산을 할 수 있을 것이다 예상 -> 틀렸습니다.
# import sys
# import heapq

# def solution(n, stars):
#     parents = [i for i in range(n)]
#     ans = 0

#     def find(star) :
#         if parents[star] != star :
#             parents[star] = find(parents[star])
#         return parents[star]
    
#     def union(star1, star2) :
#         p1 = find(star1)
#         p2 = find(star2)

#         parents[max(p1, p2)] = min(p1, p2)

#     prev = heapq.heappop(stars)
#     while stars :
#         next = heapq.heappop(stars)

#         if find(prev[3]) != find(next[3]) :
#             union(prev[3], next[3])
#             ans += ((prev[1] - next[1])**2 + (prev[2] - next[2])**2)**(1/2)
        
#         prev = next
    
#     print(f"{ans:.2f}")





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     stars = []
#     for i in range(n) :
#         x, y = map(float, input().split())
#         heapq.heappush(stars, (x**2 + y**2, x, y, i))
#     solution(n, stars)