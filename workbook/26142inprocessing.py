
# 2nd trial -> D is not big enough to overwhelm H
# counter ex
# 5
# 400 1
# 70 3
# 60 0
# 0 100
# 0 1000
# ans
# 1000
# 1401
# 1901
# 2444
# 3034
import sys

def solution(N, dragon, max_height):

    print(max_height) # 1일차
    max_height = 0
    for day in range(2, N+1) : # 2일차 - N-1일차
        res = 0
        visited = [False for _ in range(N)]
        for i in range(day-1, 0, -1) : # day일차 - 2일차 역순
            # print('in day ',day, 'in days',i, dragon[day-1-i][1] + dragon[day-1-i][0] * i,'is the biggest')
            res += dragon[day-1-i][1] + dragon[day-1-i][0] * i
            visited[day-1-i] = True
        
        for i in range(N) :
            if visited[i] :
                continue
            if max_height < dragon[i][1] :
                max_height = dragon[i][1]
        # print('and day 1', max_height)
        res += max_height

        print(res)
    return





if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    dragon = []
    max_height = 0
    for i in range(N) :
        d, h = map(int, input().split())
        if h > max_height :
            max_height = h
        dragon.append((d,h))
    
    dragon.sort(reverse=True)
    solution(N, dragon, max_height)


# 1st trial -> nice try but not the right way to solve
# import sys
# import copy
# import heapq as hq

# def solution(N, potential, heights):
    
#     for day in range(1,N+1) :
#         next_heights = copy.deepcopy(heights)
#         res = 0

#         for _ in range(day) :
#             h, i = hq.heappop(heights)
#             print('in day ',day, 'in days',_, h,'is the biggest')
#             res -= h
#             hq.heappush(next_heights,(h-potential[i],i))
#         print(res)

#         while heights :
#             h, i = hq.heappop(heights)
#             hq.heappush(next_heights,(h-potential[i],i))
        
#         heights = next_heights
#         print(heights, 'updated' )
    
#     return





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     potential, heights = [], []
#     for i in range(N) :
#         d, h = map(int, input().split())
#         potential.append(d)
#         hq.heappush(heights, (-h,i))

#     solution(N, potential, heights)