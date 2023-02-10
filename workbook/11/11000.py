import sys
import heapq as hq

def solution(N, lecture):
    lecture.sort()
    ans = [0]

    for i in range(N) :
        earlest = hq.heappop(ans)

        if earlest <= lecture[i][0] :
            hq.heappush(ans, lecture[i][1])
        else :
            hq.heappush(ans, lecture[i][1])
            hq.heappush(ans, earlest)
    
    print(len(ans))





if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    lecture = [list(map(int, input().split())) for _ in range(N)]
    
    solution(N, lecture)




# import sys
# import heapq

# def solution(N, lecture):
#     lecture.sort()
#     ans = [0]

#     for i in range(N) :
#         flag = True
#         for j in range(len(ans)) :
#             if ans[j] <= lecture[i][0] :
#                 ans[j] = lecture[i][1]
#                 flag = False
#                 break
#             if flag :
#                 ans.append(lecture[i][1])
    
#     print(len(ans))





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     lecture = [list(map(int, input().split())) for _ in range(N)]
    
#     solution(N, lecture)