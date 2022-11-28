import sys

def solution(N, M):

    def DFS(res) :

        if len(res) == M :
            print(" ".join(res))
            return

        for i in range(1,N+1) :
            DFS(res+[str(i)])  
    DFS([])


if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    solution(N, M)

