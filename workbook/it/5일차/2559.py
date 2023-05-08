import sys

def solution(N,K,temp):
    left = 0
    right = K - 1
    ans = sum(temp[:K])
    new = sum(temp[:K])

    while left < N-K:
        left += 1
        right += 1

        new = new - temp[left-1] + temp[right]
        if ans >= new:
            continue

        ans = new

    print(ans)


if __name__ == "__main__" :
    input = sys.stdin.readline
    N, K = map(int, input().split())
    temp = list(map(int, input().split()))
    solution(N,K,temp)