import sys

def solution(N, M, arr):
    def DFS(num, res) :
        if len(res) == M :
            print(" ".join(res))
            return
        
        for i in range(num, N) :
            DFS(i+1, res+[str(arr[i])])

    DFS(0,[])

if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    solution(N, M, arr)

