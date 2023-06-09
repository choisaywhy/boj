import sys

def solution(n,a):
    team = 0
    a.sort()

    for i in range(n-2):
        
        start = i+1
        end = n-1

        while start < end:
            
            if a[start] + a[end] + a[i] > 0:
                end -= 1
            elif a[start] + a[end] + a[i] < 0:
                start += 1
            else:
                if a[start] == a[end]:
                    team += (end-start)*(end-start+1)//2
                    break
                else:
                    cntstart, cntend = 0,0
                    targets, targete = a[start], a[end]
                    while a[start] == targets:
                        start += 1
                        cntstart += 1
                    while a[end] == targete:
                        end -= 1
                        cntend += 1
                    team += cntstart * cntend

    print(team)
                
        



if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int,input().split()))
    solution(n,a)






# 2nd trial wrong
# import sys
# from collections import Counter

# def solution(n,a):
#     team = 0
#     a.sort()
#     count = Counter(a)


#     for i in range(n):

#         target = a[i]
        
#         start = i+1
#         end = n-1

#         while start < end:
            
#             if a[start] + a[end] + target > 0:
#                 end -= 1
#             elif a[start] + a[end] + target < 0:
#                 start += 1
#             else:
#                 team += max(count[target],count[a[start]],count[a[end] ])

#                 break
    
#     print(team)
                
        



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     a = list(map(int,input().split()))
#     solution(n,a)




# 메모리 초과
# import sys
# from itertools import combinations

# def solution(n,a):
    
#     ans = 0
#     for t in list(combinations(a,3)):
#         if sum(t) != 0:
#             continue
#         ans += 1

#     print(ans)
        





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     a = list(map(int,input().split()))
#     solution(n,a)