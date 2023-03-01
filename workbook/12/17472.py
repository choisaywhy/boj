import sys

def solution(N,M,maps):
    islands = [0,0]
    bridges = []
    directions = [(0,1),(1,0),(0,-1),(-1,0)]


    def searchingIslands(start, curnum) :
        stack = [start]
        visited = [start]

        while stack :
            x, y = stack.pop()
            for dx, dy in directions :
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited :
                    if maps[nx][ny] == 1 :
                        visited.append((nx,ny))
                        stack.append((nx,ny))
                        maps[nx][ny] = curnum
        return (visited, curnum)


    def bulidingBridge(a) :
        island, num = a
        for x,y in island :
            stack = [(x,y,0,0),(x,y,1,0),(x,y,2,0),(x,y,3,0)] # directions의 index, 누적 dist
            
            while stack :
                x, y, direct, dist = stack.pop()
                nx, ny = x + directions[direct][0], y + directions[direct][1]
                if 0 <= nx < N and 0 <= ny < M : 
                    if maps[nx][ny] == num :
                        continue
                    elif maps[nx][ny] == 0 :
                        stack.append((nx,ny,direct,dist+1))
                    else :
                        if dist <= 1 :
                            continue
                        if (dist, num, maps[nx][ny]) not in bridges :
                            bridges.append((dist, num, maps[nx][ny]))
    

    def find(a) :
        if parents[a] != a :
            parents[a] = find(parents[a])
        return parents[a]
    
    def union(a,b) :
        pa, pb = find(a), find(b)
        parents[max(pa, pb)] = min(pa, pb)

    num = 2
    for x in range(N) :
        for y in range(M) :
            if maps[x][y] == 1 :
                maps[x][y] = num
                islands.append(searchingIslands((x,y), num))
                num += 1


    for i in range(2,len(islands)) :
        bulidingBridge(islands[i])
    
    bridges.sort(reverse=True)

    parents = [i for i in range(len(islands))]
    ans = 0
    count = 0

    while bridges :
        dist, a, b = bridges.pop()
        if find(a) == find(b) :
            continue
        union(a,b)
        ans += dist
        count += 1
        if count == len(islands)-3 :
            break

    if ans == 0 or count < len(islands)-3:
        print(-1)
    else :
        print(ans)

if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    maps = []
    for i in range(N) :
        maps.append(list(map(int, input().split())))
    
    solution(N,M,maps)



# debugging
# # import sys
# from collections import deque

# def solution(N,M,maps):
#     num = 2
#     islands = [0,0]
#     parents = [i for i in range(N+2)]
#     bridges = []
#     directions = [(0,1),(1,0),(0,-1),(-1,0)]


#     def searchingIslands(start, num) :
#         stack = [start]
#         visited = []

#         while stack :
#             x, y = stack.pop()
#             for dx, dy in directions :
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited :
#                     if maps[nx][ny] == 1 :
#                         visited.append((nx,ny))
#                         stack.append((nx,ny))
#                         maps[nx][ny] = num
#         visited.sort()
#         return (visited[0], visited[-1], num) # 섬 모양이 정사각형임을 보장할 수 없으므로, 전체 좌표를 보내야함
    
#     # 종료 조건
#     # 나 만나기
#     # 끝 만나기
#     # 다른 섬 만났는데 다리 길이 짧음
#     # 이어가기
#     # 다음 노드 바다
#     # 성공 조건
#     # 다른 섬 만났는데 다리 길이 2 초과

#     def bulidingBridge(a) :
#         start, end, num = a
#         print(start,end,num,'turn')
#         for x in range(start[0], end[0]+1) :
#             for y in range(start[1], end[1]+1) :
#                 print('x,y',x,y,'turn')
#                 stack = [(x,y,0,0),(x,y,1,0),(x,y,2,0),(x,y,3,0)] # directions의 index, 누적 dist
                
#                 while stack :
#                     x, y, direct, dist = stack.pop()
#                     nx, ny = x + directions[direct][0], y + directions[direct][1]
#                     if 0 <= nx < N and 0 <= ny < M : 
#                         if maps[nx][ny] == num :
#                             print('나를 만남',x,y,nx,ny)
#                             continue
#                         elif maps[nx][ny] == 0 :
#                             stack.append((nx,ny,direct,dist+1))
#                             print('stack updated',stack)
#                         else :
#                             if dist <= 1 :
#                                 print('dist shorter than standard',dist)
#                                 continue
#                             bridges.append((dist, num, maps[nx][ny]))
#                             print(bridges,'bridge updated')
        
#     def find(a) :
#         if parents[a] != a :
#             parents[a] = find(parents[a])
#         return parents[a]
    
#     def union(a,b) :
#         pa, pb = find(a), find(b)
#         parents[max(pa, pb)] = min(pa, pb)

#     for x in range(N) :
#         for y in range(M) :
#             if maps[x][y] == 1 :
#                 islands.append(searchingIslands((x,y), num))
#                 num += 1
    
#     print(islands)
#     print(len(islands)-3)
#     for i in range(2,len(islands)) :
#         bulidingBridge(islands[i])
    
#     bridges.sort(reverse=True)
#     ans = 0
#     count = 0
#     while bridges :
#         dist, a, b = bridges.pop()
#         if find(a) == find(b) :
#             continue
#         union(a,b)
#         ans += dist
#         count += 1

#         if count == len(islands) - 3 :
#             break
    
#     print(ans)

# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     maps = []
#     for i in range(N) :
#         maps.append(list(map(int, input().split())))
    
#     solution(N,M,maps)


# # island numbering 2부터
# import sys
# from collections import deque

# def solution(N,M,maps):
#     num = 2
#     islands = [0,0]
#     bridges = []

#     def searchingIslands(start, num) :
#         directions = [(0,1),(1,0),(0,-1),(-1,0)]
#         stack = [start]
#         visited = []

#         while stack :
#             x, y = stack.pop()
#             for dx, dy in directions :
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited :
#                     if maps[nx][ny] == 1 :
#                         visited.append((nx,ny))
#                         stack.append((nx,ny))
#                         maps[nx][ny] = num
#         visited.sort()
#         return (visited[0], visited[-1], num)
    
#     def bulidingBridge(a, b) :
#         ax1, ay1 = islands[a][0]
#         ax2, ay2 = islands[a][1]
#         bx1, by1 = islands[b][0]
#         bx2, by2 = islands[b][1]

#         temp = []

#         if (ax1 < bx2 and ax2 >= bx1) or (ax1 > bx2 and ax2 <= bx1):
#             for y in range(max(ay1, by1),min(ay2, by2)+1) :
#                 for x in range(min(ax2, bx2), max(ax1, bx1)) :
#                     if maps[x][y] == '0' :
#                         temp.append((x,y))
#                 if len(temp) <= 2 :
#                     temp = []
#                 else :
#                     break
#         if (ay1 < by2 and ay2 >= by1) or (ay1 > by2 and ay2 <= by1) :
#             # length = min(ay1 - by2, ay2 - by1)
#             # if length <= 2 :
#             #     return # 다리를 세울 수 없음
#             for x in range(max(ax1, bx1),min(ax2, bx2)+1) :
#                 for y in range(min(ay2, by2), max(ay1, by1)) :
#                     if maps[x][y] == '0' :
#                         temp.append((x,y))
#                 if len(temp) <= 2 :
#                     temp = []
#                 else :
#                     break
        
#         if temp == [] :
#             return
#         bridges.append(temp)

#         print(bridges)
#         return 
            




#     for x in range(N) :
#         for y in range(M) :
#             if maps[x][y] == 1 :
#                 islands.append(searchingIslands((x,y), num))
#                 num += 1
    
#     print(islands)
#     print(len(islands)-3)
#     for a in range(2,len(islands)-1) :
#         for b in range(a+1, len(islands)) :
#             print(a,b,'turn')
#             bulidingBridge(a,b)

#     print(bridges)


    




# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     maps = []
#     for i in range(N) :
#         maps.append(list(map(int, input().split())))
    
#     solution(N,M,maps)