import sys

input = sys.stdin.readline

M, N, K = map(int, input().split())

def hanoi(N, start, end) : # N: 원판 개수, K: 제한 시간
    if N == 1 :
        tops[end].append(tops[start].pop())
        return
    
    hanoi(N-1,start,3-start-end)
    tops[end].append(tops[start].pop())
    hanoi(N-1,3-start-end,end)

def hanoi3(N,K) :
    pass
def hanoi4(N,K) :
    pass


tops = [[i for i in range(N-1,-1,-1)], [], []]
if M == 1:
    hanoi(N,0,2) 
    print(tops)
elif M == 2:
    hanoi3(N,K)
elif M == 3:
    hanoi4(N,K)
