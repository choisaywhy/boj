import sys

def solution(N, L, roads):
    ans = 0

    def pathfinder(road):
        nonlocal ans
        flag = True
        if len(road) == 1:
            ans += 1
            return

        for i in range(1,len(road)):
            if road[i-1][0] - 1 == road[i][0]:
                if road[i][1] < L:
                    flag = False
                    break
                road[i][1] -= L
            elif road[i-1][0] + 1 == road[i][0]:
                if road[i-1][1] < L:
                    flag = False
                    break
                road[i-1][1] -= L
            else:
                flag = False
                break

        if flag:
            ans += 1
        return

    def road_count(road):
        new_road = []
        count = 1
        for i in range(1,N):
            prev = road[i-1]
            if prev == road[i]:
                count += 1
            else:
                new_road.append([prev, count])
                count = 1

        new_road.append([road[N-1], count])
        return new_road

    for i in range(N):
        pathfinder(road_count(roads[i]))
        pathfinder(road_count([roads[j][i] for j in range(N)]))
    print(ans)



if __name__ == "__main__" :
    input = sys.stdin.readline
    N, L = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(N)]
    solution(N, L, roads)



# debugging ver
# import sys

# def solution(N, L, roads):
#     ans = 0

#     def pathfinder(road):
#         nonlocal ans
#         flag = False
#         if len(road) == 1:
#             ans += 1
#             print('available',road)

#             return

#         for i in range(1,len(road)):
#             prev, prev_count = road[i-1]
#             cur, cur_count = road[i]
#             if prev - 1 == cur:
#                 if cur_count < L:
#                     flag = True
#                     break
#                 road[i][1] -= L
#             elif prev + 1 == cur:
#                 if prev_count < L:
#                     flag = True
#                     break
#                 road[i-1][1] -= L
#             else:
#                 flag = True
#                 break

#         if not flag:
#             ans += 1
#             print('available',road)

#         return

#     def road_count(road):
#         prev = road[0]
#         new_road = []
#         count = 1
#         for i in range(1,N):
#             if prev == road[i]:
#                 count += 1
#             else:
#                 new_road.append([prev, count])
#                 count = 1
#             prev = road[i]

#         new_road.append([prev, count])
#         return new_road

#     for i in range(N):
#         print(i,'행')
#         pathfinder(road_count(roads[i]))
#         print(i,'열')
#         pathfinder(road_count([roads[j][i] for j in range(N)]))
#     print(ans)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, L = map(int, input().split())
#     roads = [list(map(int, input().split())) for _ in range(N)]
#     solution(N, L, roads)