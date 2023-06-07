# 이분탐색
import sys

def solution(n,cards,m,guess):
    
    def lower_index(target):
        start = 0
        end = n

        while start < end:
            mid = (start+end) // 2

            if cards[mid] >= target:
                end = mid
            else:
                start = mid + 1
        
        return start
    
    def upper_index(target):
        start = 0
        end = n

        while start < end:
            mid = (start+end) // 2

            if cards[mid] > target:
                end = mid
            else:
                start = mid + 1

        return start
    
    cards.sort()
    for g in guess:
        print(upper_index(g) - lower_index(g), end=' ')



if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    cards = list(map(int, input().split()))
    m = int(input())
    guess = list(map(int, input().split()))
    solution(n,cards,m,guess)


# counter
# import sys
# from collections import Counter

# def solution(n,cards,m,guess):
#     count = Counter(cards)
    
#     for g in guess:
#         print(count[g],end=" ")


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     cards = list(map(int, input().split()))
#     m = int(input())
#     guess = list(map(int, input().split()))
#     solution(n,cards,m,guess)