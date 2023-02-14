# 코드 개선
import sys

def solution(N, days):
    profit = 0
    highest = days[-1]

    for i in range(N-2, -1, -1) :
        if highest >= days[i] :
            profit += highest - days[i]
        else :
            highest = days[i]
    
    print(profit)



if __name__ == "__main__" :
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T) :
        N = int(input())
        days = list(map(int, input().split()))
        solution(N, days)



# 정답 코드
# import sys

# def solution(N, days):
#     profit = 0
#     stack = [days[-1]]

#     for i in range(N-1, -1, -1) :
#         if stack[-1] >= days[i] :
#             profit += stack[-1] - days[i]
#         else :
#             stack.pop()
#             stack.append(days[i])
    
#     print(profit)





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     T = int(input())
#     for _ in range(T) :
#         N = int(input())
#         days = list(map(int, input().split()))
#         solution(N, days)


# 가장 큰 수가 맨 뒤에 나오는 경우 고려 못함
# 반례
# 1 2 3 2 4 (답 : 8, 실행결과 : 5)
# import sys

# def solution(N, days):
#     profit = 0
#     count = 0
#     ans = 0

#     for i in range(N-1) :
#         if days[i] <= days[i+1] :
#             count += 1
#             profit += (days[i+1] - days[i]) * count
#         else : # 증가 종료
#             ans += profit
#             profit = 0
#             count = 0
#     ans += profit
    
#     print('answer is',ans,end='\n')





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     T = int(input())
#     for _ in range(T) :
#         N = int(input())
#         days = list(map(int, input().split()))
#         solution(N, days)