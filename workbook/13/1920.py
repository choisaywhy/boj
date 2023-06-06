import sys

def solution(n,a,m,x):
    a = set(a) ### set 없으면 시간초과 뜸
    
    for target in x:
        if target in a:
            print(1)
            continue
        print(0)
        



if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    x = list(map(int, input().split()))
    solution(n,a,m,x)


# 이분탐색 정석 풀이
# import sys

# def solution(n,a,m,x):
#     a.sort()
    
#     for target in x:
        
#         start = 0
#         end = n-1
#         flag = False

#         while start <= end:
#             mid = (start+end)//2

#             if a[mid] < target:
#                 start = mid + 1
#             elif a[mid] > target:
#                 end = mid - 1
#             else:
#                 flag = True
#                 break
        
#         if flag:
#             print(1)
#         else:
#             print(0)
                





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     a = list(map(int,input().split()))
#     m = int(input())
#     x = list(map(int, input().split()))
#     solution(n,a,m,x)