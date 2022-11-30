import sys

def solution(N, M, arr):

    def DFS(index, res) :
        if len(res) == M :
            print(" ".join(map(str, res)))
            return
        
        revalue = 0
        for i in range(index, N) :
            if arr[i] == revalue :
                continue
            revalue = arr[i]
            DFS(i+1, res+[arr[i]])
        
    DFS(0, [])

if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    solution(N, M, arr)


