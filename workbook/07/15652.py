import sys

def solution(N, M):

    def DFS(num,res) :

        if len(res) == M :
            print(" ".join(res))
            return

        for i in range(num,N+1) :
            DFS(i,res+[str(i)])  
    DFS(1,[])


if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    solution(N, M)

