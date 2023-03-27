import sys
def solution(N, curve, maps):
    directions = [(1,0),(0,-1),(-1,0),(0,1)]

    def dragonCurve(cur_curve):
        x,y,d,g = cur_curve
        stack = [d]
        maps[x][y] = True

        for _ in range(g):
            for i in range(len(stack)-1, -1, -1):
                stack.append((stack[i]+1)%4)
        
        for i in range(len(stack)):
            x += directions[stack[i]][0]
            y += directions[stack[i]][1]

            if not (0 <= x < 101 and 0 <= y < 101):
                continue

            maps[x][y] = True
    
    for cur_curve in curve:
        dragonCurve(cur_curve)

    ans = 0
    for x in range(100):
        for y in range(100):
            if maps[x][y] and maps[x+1][y] and maps[x][y+1] and maps[x+1][y+1]:
                ans += 1

    print(ans)


if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    maps = [[False] * 101 for _ in range(101)]
    curve = [tuple(map(int, input().split())) for _ in range(N)]
    solution(N, curve, maps)



# import sys
# # 90도 회전 시 규칙 찾아내는 중
# def solution(N, curve, maps):
#     directions = [(1,0),(0,-1),(-1,0),(0,1)]

#     def dragonCurve(cur_curve):
#         x,y,d,g = cur_curve
#         stack = [d]
#         maps[x][y] = True

#         for _ in range(g):
#             for i in range(len(stack)-1, -1, -1):
#                 stack.append((stack[i]+1)%4)
        
#         for i in range(len(stack)):
#             x += directions[stack[i]][0]
#             y += directions[stack[i]][1]

#             if not (0 <= x < 101 and 0 <= y < 101):
#                 continue

#             maps[x][y] = True
    
#     for cur_curve in curve:
#         dragonCurve(cur_curve)

#     ans = 0
#     for x in range(101):
#         for y in range(101):
#             if maps[x][y] and maps[x+1][y] and maps[x][y+1] and maps[x+1][y+1]:
#                 ans += 1

#     print(ans)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     maps = [[False] * 101 for _ in range(101)]
#     curve = [tuple(map(int, input().split())) for _ in range(N)]
#     solution(N, curve, maps)