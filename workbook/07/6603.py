import sys

def solution(k, S) :
    def DFS(index, res) :
        if len(res) == 6 :
            print(" ".join(map(str, res)))
            return

        for i in range(index, len(S)) :
            DFS(i+1, res + [S[i]])
    
    DFS(0,[])



if __name__ == "__main__" :
    input = sys.stdin.readline
    while True :
        arr = list(map(int, input().split()))
        if arr[0] == 0 :
            break
        solution(arr[0], arr[1:])
        print()