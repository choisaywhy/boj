import sys
from collections import deque
def solution(S, T):
    ans = False
    def DFS(tempT):
        nonlocal ans
        if len(tempT) == len(S):
            if tempT == S:
                ans = True
            return
        
        if tempT[-1] == "A":
            DFS(tempT[:-1])
        if tempT[0] == "B":
            DFS(tempT[-1:0:-1])

    
    DFS(T)
    print(1 if ans else 0)






if __name__ == "__main__" :
    input = sys.stdin.readline
    S = input().strip()
    T = input().strip()

    solution(S, T)