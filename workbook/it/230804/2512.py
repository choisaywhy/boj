import sys

def solution():
    n = int(input())
    req = list(map(int,input().split()))
    m = int(input())

    if sum(req) <= m: # 예산요청을 상한액 없이 배정
        print(max(req))
    else: # 상한액 지정
        start = 0
        end = max(req)

        while start <= end:
            mid = (start+end) // 2
            budget = 0

            for r in req: # 상한액 당 총 예산
                if r <= mid:
                    budget += r
                else:
                    budget += mid

            if budget > m:
                end = mid - 1
            else:
                start = mid + 1
            

        print(end)



if __name__ == "__main__" :
    input = sys.stdin.readline
    
    solution()
