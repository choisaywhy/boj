import sys
import heapq as hq

def solution(n,m,cards):
    hq.heapify(cards)

    for _ in range(m) :
        x = hq.heappop(cards)
        y = hq.heappop(cards)

        hq.heappush(cards, x+y)
        hq.heappush(cards, x+y)
    
    print(sum(cards))
    




if __name__ == "__main__" :
    input = sys.stdin.readline
    n, m = map(int, input().split())

    cards = list(map(int, input().split()))

    solution(n,m,cards)