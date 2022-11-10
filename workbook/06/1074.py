import sys

input = sys.stdin.readline


def solution(N,r,c,count) :
    if N == 2:
        if r == 0 and c == 0:
            count += 0
        elif r == 0 and c == 1:
            count += 1
        elif r == 1 and c == 0:
            count += 2
        elif r == 1 and c == 1:
            count += 3
        return count
    
    if r < N//2 and c < N//2: # 2사분면
        count = solution(N//2, r, c, count)
    elif r < N//2 and c >= N//2: # 1사분면
        count = solution(N//2, r, c-N//2, count+(N//2)**2)
    elif r >= N//2 and c < N//2: # 3사분면
        count = solution(N//2, r-N//2, c, count+((N//2)**2)*2)
    elif r >= N//2 and c >= N//2: # 4사분면
        count = solution(N//2, r-N//2, c-N//2, count+((N//2)**2)*3)
    
    return count

N, r, c = map(int, input().split())
print(solution(2**N,r,c,0))