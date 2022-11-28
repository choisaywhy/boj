import sys

def solution(L, C, arr):

    def DFS(num, res) :
        if len(res) == L :
            count = 0
            for r in res :
                if r in ['a','e','i','o','u'] :
                    count += 1
            if count < 1 or L - count < 2 :
                return
            print("".join(res))
            return

        for i in range(num, C) :
            DFS(i+1, res+arr[i])

    DFS(0, "")

if __name__ == "__main__" :
    input = sys.stdin.readline
    L, C = map(int, input().split())
    arr = sorted(list(map(str, input().split())))
    solution(L, C, arr)


