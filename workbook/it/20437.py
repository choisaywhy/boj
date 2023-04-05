import sys

def solution(W, K):
    word = {}
    for idx in range(len(W)):
        word[W[idx]] = word.get(W[idx],[]) + [idx]
    
    aqua, raquator = 10001, 0

    for w, idx in word.items():

        if len(idx) < K:
            continue

        for i in range(len(idx)-K+1):
            # aqua 구하기
            aqua = min(idx[i+K-1]-idx[i]+1, aqua)
            # raquator 구하기
            raquator = max(idx[i+K-1]-idx[i]+1, raquator)

    if aqua == 10001 or raquator == 0:
        print(-1)
    else:
        print(aqua, raquator)



if __name__ == "__main__" :
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        W = input().strip()
        K = int(input())
        solution(W, K)


# debugging ver
# import sys

# def solution(W, K):
#     word = {}
#     for idx in range(len(W)):
#         word[W[idx]] = word.get(W[idx],[]) + [idx]
    
#     aqua, raquator = 10001, 0

#     for w, idx in word.items():
#         print(w,idx,'turn')

#         if len(idx) < K:
#             print(K,'개 만족 못함 넘어가기')
#             continue

#         for i in range(len(idx)-K+1):
#             print(i, i+K-1,'번째 살펴보기', idx[i],idx[i+K-1])
#             # aqua 구하기
#             aqua = min(idx[i+K-1]-idx[i]+1, aqua)
#             # raquator 구하기
#             raquator = max(idx[i+K-1]-idx[i]+1, raquator)
#             print('aqua',aqua)
#             print('raquator',raquator)

#     if aqua == 10001 or raquator == 0:
#         print(-1)
#     else:
#         print(aqua, raquator)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     T = int(input())
#     for _ in range(T):
#         W = input().strip()
#         K = int(input())
#         solution(W, K)