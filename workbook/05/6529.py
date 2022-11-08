import sys

input = sys.stdin.readline

while True :
    heights = list(map(int, input().split()))
    N = heights[0]
    if N == 0 :
        break
    heights = heights[1:]
    areas = []
    stack = []



    for h in range(N) :
        width = -1
        while stack and stack[-1][0] > heights[h] : 
            height, width = stack.pop()
            areas.append((h-width)*height)

        if stack and stack[-1][0] == heights[h] :
            continue
        
        if width > -1 :
            stack.append([heights[h], width])
        else :
            stack.append([heights[h], h])



    if stack :
        for h,w in stack :
            areas.append(h*(N-w))

    print(max(areas))



# debugging
# import sys

# input = sys.stdin.readline

# while True :
#     heights = list(map(int, input().split()))
#     N = heights[0]
#     if N == 0 :
#         break
#     heights = heights[1:]
#     areas = []
#     stack = []



#     for h in range(N) :
#         width = -1
#         print('index',h, heights[h],'turn')
#         while stack and stack[-1][0] > heights[h] : 
#             height, width = stack.pop()
#             areas.append((h-width)*height)
#             print('areas updated',areas)

#         if stack and stack[-1][0] == heights[h] :
#             print('got same height')
#             continue
        
#         if width > -1 :
#             stack.append([heights[h], width])
#         else :
#             stack.append([heights[h], h])

#         print('stack updated to',stack)


#     if stack :
#         print('final left stack',stack)
#         for h,w in stack :
#             areas.append(h*(N-w))
#         print('stack updated to',areas)

#     print('result is ',max(areas))






# import sys

# input = sys.stdin.readline

# while True :
#     heights = list(map(int, input().split()))
#     N = heights[0]
#     if N == 0 :
#         break
#     heights = heights[1:]
#     areas = []
#     stack = []


#     for h in range(N) :
#         nextwidth = 0
#         print('index',h, heights[h],'turn')
#         while stack and stack[-1][0] > heights[h] : 
#             nextheight, nextwidth = stack.pop()
#             areas.append(nextwidth*nextheight)
#             print('areas updated',areas)

#         if not stack :
#             print('stack is empty')
#             stack.append([heights[h], 1+nextwidth])
#             print('stack updated to',stack)
#             continue
        
#         if stack[-1][0] == heights[h] :
#             print('got same height')
#             stack[-1][1] += 1
#             print('stack updated to',stack)
#             continue

#         for i in range(len(stack)-1, -1, -1) :
#             if stack[i][0] < heights[h] :
#                 stack[i][1] += 1
#         stack.append([heights[h], 1])
#         print('stack updated to',stack)



#     if stack :
#         print('final stack')
#         for h,w in stack :
#             areas.append(h*w)
#         print('stack updated to',areas)

#     print('result is ',max(areas))







# import sys

# input = sys.stdin.readline

# while True :
#     heights = list(map(int, input().split()))
#     N = heights[0]
#     if N == 0 :
#         break
#     heights = heights[1:]
#     areas = []
#     stack = []


#     for h in range(N) :
#         nextwidth = 0
#         print('index',h, heights[h],'turn')
#         while stack and stack[-1][0] > heights[h] : 
#             nextheight, nextwidth = stack.pop()
#             areas.append(nextwidth*nextheight)
#             print('areas updated',areas)

#         if not stack :
#             print('stack is empty')
#             stack.append([heights[h], 1+nextwidth])
#             print('stack updated to',stack)
#             continue

#         if stack[-1][0] == heights[h] :
#             print('got same height')
#             stack[-1][1] += 1
#             continue
#             print('stack updated to',stack)

#         for i in range(len(stack)-1, -1, -1) :
#             if stack[i][0] < heights[h] :
#                 stack[i][1] += 1
#         stack.append([heights[h], 1])
#         print('stack updated to',stack)



#     if stack :
#         print('final stack')
#         for h,w in stack :
#             areas.append(h*w)
#         print('stack updated to',areas)

#     print('result is ',max(areas))




