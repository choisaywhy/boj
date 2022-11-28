import sys

def solution(N,M,arr) :
    def DFS(res) :
        if len(res) == M :
            print(" ".join(res))
            return
        
        for i in range(N) :
            DFS(res+[str(arr[i])])

    DFS([])




if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    solution(N,M,arr)