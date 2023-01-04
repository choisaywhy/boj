import sys

def solution(N, K, coins):
    index = N-1
    count = 0
    while K > 0 :
        if coins[index] <= K :
            count += K // coins[index]
            K %= coins[index]
        index -= 1
    
    print(count)





if __name__ == "__main__" :
    input = sys.stdin.readline
    N, K = map(int, input().split())
    coins = []
    for _ in range(N) :
        coins.append(int(input()))
    solution(N, K, coins)