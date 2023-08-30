# 런타임에러 디버깅 중
import sys
from copy import deepcopy
input = sys.stdin.readline

n, k = map(int,input().split())
flour = list(map(int,input().split()))
max_flour, min_flour = 0,0
dx = [0,1]
dy = [1,0]

def compare_with_k():
    global max_flour, min_flour
    max_flour = max(flour)
    min_flour = min(flour)
    
    return False if max_flour - min_flour > k else True


def add_one_to_smallest():
    global flour

    for i in range(n):
        if flour[i] > min_flour:
            continue
        flour[i] += 1
    

def roll_up():
    depth = 1 # 같은 길이로 2번 0,1
    length = 1 # 길이
    leftovers = n-1 # 남은 일자 밀가루
    dough = [[0]*10 for _ in range(10)]
    dough[0][0] = flour[0]
    
    while length <= leftovers:
        tmp = [[0]*(length+depth) for _ in range(length)]
        # 기존 도우 돌리기
        for x in range(length+depth):
            for y in range(length):
                tmp[y][length-1-x] = dough[x][y]
        # 새로운 줄 추가해서 dough update
        for x in range(length):
            for y in range(length+depth):
                dough[x][y] = tmp[x][y]

        x = length - 1 if depth == 0 else length
        for y in range(length):
            dough[x][y] = flour[(n-leftovers)+y]

        # roll up update
        leftovers -= length
    
        if depth == 1:
            length += 1
            depth = 0
        else:
            depth = 1
    # 남은 도우 더해주기
    x = length - 1 if depth == 0 else length
    if leftovers > 0:
        for y in range(leftovers):
            dough[x][length+y-1] = flour[n-(leftovers - y)]

    return dough, x+1, length+leftovers-1


def press(dough,row,col):
    global flour

    # 인접 도우 연산
    tmp = deepcopy(dough)
    for x in range(row):
        for y in range(col):
            if dough[x][y] == 0:
                continue
            for i in range(2):
                nx,ny = dx[i]+x, dy[i]+y
                if not( 0<= nx < row and 0<= ny < col):
                    continue
                if dough[nx][ny] == 0:
                    continue
                d = abs(dough[x][y] - dough[nx][ny])//5
                if d > 0:
                    if dough[x][y] > dough[nx][ny]:
                        tmp[x][y] -= d
                        tmp[nx][ny] += d
                    else:
                        tmp[x][y] += d
                        tmp[nx][ny] -= d
    flour = []
    # 도우 누르기
    for y in range(col):
        for x in range(row-1,-1,-1):
            if tmp[x][y] == 0:
                continue
            flour.append(tmp[x][y])


def fold_half():
    length = n//4
    dough = []

    dough.append(list(reversed(flour[length*2:length*3])))
    dough.append(flour[length:length*2])
    dough.append(list(reversed(flour[:length])))
    dough.append(flour[length*3:])

    return dough, 4, length


turns = 0
while not compare_with_k():
    turns += 1

    add_one_to_smallest()
    dough, row, col = roll_up()
    press(dough, row, col)
    
    dough, row, col = fold_half()
    press(dough, row, col)

print(turns)





############ debugging ver
# import sys
# from copy import deepcopy
# input = sys.stdin.readline

# n, k = map(int,input().split())
# flour = list(map(int,input().split()))
# max_flour, min_flour = 0,0
# dx = [0,1]
# dy = [1,0]

# def compare_with_k():
#     global max_flour, min_flour
#     max_flour = max(flour)
#     min_flour = min(flour)
    
#     return False if max_flour - min_flour > k else True


# def add_one_to_smallest():
#     global flour

#     for i in range(n):
#         if flour[i] > min_flour:
#             continue
#         flour[i] += 1
    

# def roll_up():
#     depth = 1 # 같은 길이로 2번 0,1
#     length = 1 # 길이
#     leftovers = n-1 # 남은 일자 밀가루
#     dough = [[0]*10 for _ in range(10)]
#     dough[0][0] = flour[0]
    
#     while length <= leftovers:
#         tmp = [[0]*(length+depth) for _ in range(length)]
#         print('turns of depth',depth,'lenght',length)
#         # 기존 도우 돌리기
#         for x in range(length+depth):
#             for y in range(length):
#                 tmp[y][length-1-x] = dough[x][y]
#         print('turned tmp',tmp)
#         # 새로운 줄 추가해서 dough update
#         for x in range(length):
#             for y in range(length+depth):
#                 dough[x][y] = tmp[x][y]

#         x = length - 1 if depth == 0 else length
#         for y in range(length):
#             dough[x][y] = flour[(n-leftovers)+y]
#         print('updated dough',dough)

#         # roll up update
#         leftovers -= length
    
#         if depth == 1:
#             length += 1
#             depth = 0
#         else:
#             depth = 1
#     # 남은 도우 더해주기
#     x = length - 1 if depth == 0 else length
#     if leftovers > 0:
#         for y in range(leftovers):
#             dough[x][length+y-1] = flour[n-(leftovers - y)]

#     return dough, x+1, length+leftovers-1


# def press(dough,row,col):
#     global flour
#     print("pressing",dough)
#     print("row col",row,col)

#     # 인접 도우 연산
#     tmp = deepcopy(dough)
#     for x in range(row):
#         for y in range(col):
#             if dough[x][y] == 0:
#                 continue
#             for i in range(2):
#                 nx,ny = dx[i]+x, dy[i]+y
#                 if not( 0<= nx < row and 0<= ny < col):
#                     continue
#                 print("about to see nx,ny",nx,ny)
#                 if dough[nx][ny] == 0:
#                     continue
#                 d = abs(dough[x][y] - dough[nx][ny])//5
#                 if d > 0:
#                     if dough[x][y] > dough[nx][ny]:
#                         tmp[x][y] -= d
#                         tmp[nx][ny] += d
#                     else:
#                         tmp[x][y] += d
#                         tmp[nx][ny] -= d
#     print("after operating d",tmp)
#     flour = []
#     # 도우 누르기
#     for y in range(col):
#         for x in range(row-1,-1,-1):
#             if tmp[x][y] == 0:
#                 continue
#             flour.append(tmp[x][y])


# def fold_half():
#     length = n//4
#     dough = []

#     dough.append(list(reversed(flour[length*2:length*3])))
#     dough.append(flour[length:length*2])
#     dough.append(list(reversed(flour[:length])))
#     dough.append(flour[length*3:])

#     return dough, 4, length


# turns = 0
# while not compare_with_k():
#     turns += 1

#     add_one_to_smallest()
#     dough, row, col = roll_up()
#     print("rolled up",dough)
#     press(dough, row, col)

    
#     dough, row, col = fold_half()
#     print("fold_half",dough)

#     press(dough, row, col)
#     print("updated dough for turn",turns,flour)

# print(turns)


