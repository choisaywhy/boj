import sys

def solution(n, skylines):
    stack = []
    building = 0

    for skyline in skylines:
        x, y = skyline

        if not stack or stack[-1] < y:
            if y != 0:
                stack.append(y)
            continue
        

        while stack and stack[-1] >=y:
            if stack.pop() == y:
                break
            building += 1

        if y == 0:
            continue
        stack.append(y)
    
    building += len(stack)

    print(building)


if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    skylines = list(tuple(map(int, input().split())) for _ in range(n))
    solution(n, skylines)



# debugging ver
# import sys

# def solution(n, skylines):
#     stack = []
#     building = 0

#     for skyline in skylines:
#         x, y = skyline
#         print(x,y,'turn')

#         if not stack or stack[-1] < y:
#             if y == 0:
#                 continue
#             print('stack 에 추가',y)
#             stack.append(y)
#             print(stack,'updated')
#             continue
        

#         while stack and stack[-1] >=y:
#             if stack.pop() == y:
#                 print('과 높이 같음 넘어감')
#                 break
#             print('보다 작음, 빌딩 하나 끝남')
#             building += 1
#             print(building,'빌딩 업데이트')
#             print(stack,'updtaetd')

#         if y == 0:
#             continue
#         stack.append(y)
#         print(stack,'updated')
    
#     building += len(stack)

#     print(building)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     skylines = list(tuple(map(int, input().split())) for _ in range(n))
#     solution(n, skylines)