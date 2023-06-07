# 이분탐색
import sys

def solution(n,x):
    tmp = sorted(list(set(x)))

    # 이분 탐색
    for target in x:        
        start = 0
        end = len(tmp)-1

        while start < end:
            mid = (start + end) // 2
            if tmp[mid] >= target:
            
                end = mid
            else:
                start = mid + 1
        
        print(end, end=" ")

    



if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    x = list(map(int, input().split()))
    solution(n,x)




# using dict
# import sys

# def solution(n,x):
    
    
#     count = {}
#     for idx, v in enumerate(sorted(list(set(x)))):
#         count[v] = idx
    
#     for i in x:
#         print(count[i], end = " ")






# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     x = list(map(int, input().split()))
#     solution(n,x)