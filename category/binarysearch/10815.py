import sys


input = sys.stdin.readline
N = int(input())
card = list(map(int,input().split()))
M = int(input())
guess = list(map(int,input().split()))

card.sort()


for g in guess :
    mid = 0
    start = 0
    end = len(card) - 1
    flag = False

    while start <= end :
        mid = (start + end) // 2
        if card[mid] < g :
            start = mid + 1
        elif card[mid] > g :
            end = mid - 1
        else :
            flag = True
            break
    if flag :
        print(1,end=" ")
    else :
        print(0,end=" ")
        
