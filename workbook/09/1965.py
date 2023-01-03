import sys

def solution(n, boxes):
    dp = [1] * n

    for i in range(1,n) :
        for j in range(i) :
            if boxes[j] < boxes[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j]+1
    print(max(dp))




if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    boxes = list(map(int, input().split()))
    solution(n, boxes)