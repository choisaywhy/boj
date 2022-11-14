# arr가 별도 지정 없이 전역변수가 되는지
# -> 가능, 함수 호출 전 선언했으므로, pattern이 할당되고나서 함수가 실행되었을 것.
# -> 실행 결과 메모리와 시간이 더욱 적게 들었다.
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def star(N):
    if N == 3:
        pattern[1][:3] = ["*", " ", "*"]
        pattern[0][:3] = pattern[2][:3] = ['*']*3
        return 
    
    star(N//3)

    for i in range(0, N, N//3) : # 총 iter 횟수가 3이 되도록
        for j in range(0, N, N//3) :
            if i != N//3 or j != N//3 : # 9개 조각 중, 5번째 조각 제외
                for l in range(N//3) :
                    pattern[i+l][j:j+N//3] = pattern[l][:N//3]
    


N = int(input())
if N == 3:
    print("***","* *","***", sep="\n")
else :
    pattern = [[" "]*N for _ in range(N)] 
    star(N)

    for i in range(N) :
        for j in range(N) :
            print(pattern[i][j] , end="")
        print()


# arr 지역 변수
# import sys

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def star(N, pattern):
#     if N == 3:
#         pattern[1][:3] = ["*", " ", "*"]
#         pattern[0][:3] = pattern[2][:3] = ['*']*3
#         return pattern
    
#     pattern = star(N//3, pattern)

#     for i in range(0, N, N//3) : # 총 iter 횟수가 3이 되도록
#         for j in range(0, N, N//3) :
#             if i != N//3 or j != N//3 : # 9개 조각 중, 5번째 조각 제외
#                 for l in range(N//3) :
#                     pattern[i+l][j:j+N//3] = pattern[l][:N//3]
    
#     return pattern



# N = int(input())
# if N == 3:
#     print("***","* *","***", sep="\n")
# else :
#     pattern = [[" "]*N for _ in range(N)]
#     pattern = star(N, pattern)

#     for i in range(N) :
#         for j in range(N) :
#             print(pattern[i][j] , end="")
#         print()