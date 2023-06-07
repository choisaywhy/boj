## 범위 잡는 연습
# debugging
import sys

def solution(k,n,lan):

    start = 1
    end = min(lan)

    # upper index
    while start < end:
        mid = (start + end+1) // 2
        

        target = 0
        for l in lan:
            target += l // mid
        if n <= target:
            start = mid
        else:
            end = mid -1

    
    print(end)






if __name__ == "__main__" :
    input = sys.stdin.readline
    k,n = map(int, input().split())
    lan = list(int(input()) for _ in range(k))
    solution(k,n,lan)