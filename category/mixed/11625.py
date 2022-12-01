import sys


def solution(cards):
    count = {}

    for card in cards :
        count[card] = count.get(card, 0) + 1
    
    maximum = sorted(count.values())[-1]

    for k in sorted(count.keys()) :
        if count[k] == maximum :
            return k    

N = int(sys.stdin.readline())
cards = [ int(sys.stdin.readline()) for _ in range(N)]

print(solution(cards))