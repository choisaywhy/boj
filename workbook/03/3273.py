# 통과 -> visited 확인
import sys
def solution(n,a,x):
    count = 0
    exists = [0] * 2000001

    for i in a :
        if exists[x-i] == 1 :
            count += 1
        exists[i] = 1

    print(count)

    

if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    solution(n,a,x)




# 시간 초과 -> dfs
# import sys
# def solution(n,a,x):
#     count = 0

#     def DFS(index ,res) :
#         nonlocal count
#         if len(res) == 2 :
#             if sum(res) == x :
#                 count += 1
#             return
        
#         for i in range(index, n) :
#             DFS(i+1, res+[a[i]])
        
#     DFS(0, [])
#     print(count)

    

# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     a = list(map(int, input().split()))
#     x = int(input())
#     solution(n,a,x)



# 시간 초과 -> combinations 사용
# import sys
# from itertools import combinations
# def solution(n,a,x):
#     count = 0
#     for c in combinations(a, 2) :
#         if x == sum(c) :
#             count +=1

#     print(count)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     a = list(map(int, input().split()))
#     x = int(input())
#     solution(n,a,x)


# 시간초과 -> 반복문 사용
# import sys
# def solution(n,a,x):
#     count = 0
#     for i in range(n-1) :
#         for j in range(i, n):
#             if a[i] + a[j] == x :
#                 count += 1

#     print(count)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     a = list(map(int, input().split()))
#     x = int(input())
#     solution(n,a,x)