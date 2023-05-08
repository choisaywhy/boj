import sys
from collections import deque

def solution(N):
    dp = [False]*(N+1)

    queue = deque([(N, 0, [N])]) # 현재 수, depth, process

    while queue:
        num, depth, process = queue.popleft()

        if num == 1:
            print(depth)
            print(" ".join(map(str, process)))
            break
        
        if num % 3 == 0 and not dp[num//3]:
            queue.append((num//3, depth+1, process+[num//3]))
            dp[num//3] = True

        if num % 2 == 0 and not dp[num//2]:
            queue.append((num//2, depth+1, process+[num//2]))
            dp[num//2] = True
        
        if num-1 > -1 and not dp[num-1]:
            queue.append((num-1, depth+1, process+[num-1]))
            dp[num-1] = True



if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    solution(N)