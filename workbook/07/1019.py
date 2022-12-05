import sys
from collections import Counter

def solution(N) :
    res = [0 for _ in range(10)]
    count = 0
    while N != 0 :
        while N % 10 != 9 :
            for i in str(N) :
                res[int(i)] += 10**count
            N -= 1
        if N < 10 :
            for i in range(N + 1) :
                res[int(i)] += 10**count
            res[0] -= 10**count
            break
        for i in range(10) :
            res[i] += (N // 10 +1) * 10 ** count
        res[0] -= 10**count
        count += 1
        N //= 10
    
    print(" ".join(map(str, res)))


if __name__ == "__main__" :
    input= sys.stdin.readline
    N = int(input())
    solution(N)




# 무지성
# import sys
# from collections import Counter

# def solution(N) :
#     res = ""
#     for i in range(1,N+1) :
#         res += str(i)
#     count = Counter(res)

#     for i in range(10) :
#         print(i,':',count[str(i)])

# if __name__ == "__main__" :
#     input= sys.stdin.readline
#     N = int(input())
#     solution(N)