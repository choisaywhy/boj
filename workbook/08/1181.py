import sys

def solution(N, arr):
    for word in sorted(set(arr)) :
        print(word[1])




if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    arr = []
    for _ in range(N) :
        word = str(input().strip())
        arr.append((len(word), word))
    solution(N, arr)