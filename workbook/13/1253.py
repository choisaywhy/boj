# https://latte-is-horse.tistory.com/314

# 배열 목록에 음수가 존재하기 때문에, k의 idx가 항상 i,j의 것보다 크다는 것은 오류이다


import sys

def solution(n,a):
    a.sort()
    ans = 0

    for i in range(n):
        tmp = a[:i] + a[i+1:] 
        start = 0
        end = len(tmp) - 1
        while start < end:
            target = tmp[start] + tmp[end]
            if target < a[i]:
                start += 1
            elif target > a[i]:
                end -= 1
            else:
                ans += 1
                break

    
    print(ans)





if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    solution(n,a)




# 중복 처리 안됨
# import sys

# def solution(n,a):
#     a.sort()
#     ans = 0
#     visited = [False]*n

#     for i in range(n-2):
#         for j in range(i+1,n-1):
#             print(a[i],'i',a[j],'j turn')
#             start = j+1
#             end = n-1

#             while start <= end:
#                 mid = (start + end) // 2
#                 print('start',start,'end',end,'mid',mid)
#                 print(a[mid] , a[i] , a[j])


#                 if a[mid] < a[i] + a[j]:
#                     start = mid + 1
#                 elif a[mid] > a[i] + a[j]:
#                     end = mid - 1
#                 else:
#                     if not visited[mid]:
#                         ans += 1
#                         visited[mid] = True
#                         print('kicked the hit')
#                     break
#     print(ans)
                


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     a = list(map(int, input().split()))
#     solution(n,a)



# 1st trial
# import sys

# def solution(n,a):
#     a.sort()
#     ans = 0

#     for i in range(n-2):
#         j = i + 1
#         k = n - 1
#         while j < k < n:
#             target = a[k] - (a[i]+a[j])

#             if target > 0:
#                 j += 1
#             elif target < 0:
#                 k -= 1
#             else:
#                 cntk, targetk = 0, a[k]
#                 while k<n and targetk == a[k]:
#                     k += 1
#                     cntk += 1
#                 ans += 1
    
#     print(ans)





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     a = list(map(int, input().split()))
#     solution(n,a)