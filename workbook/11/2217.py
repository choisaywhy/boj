import sys

def solution(N,rope):
    rope.sort(reverse = True)
    maxi = 0
    for i in range(N) :
        if rope[i] * (i+1) > maxi :
            maxi = rope[i] * (i+1)
    print(maxi)




if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    rope = []
    for _ in range(N) :
        rope.append(int(input()))
    solution(N,rope)