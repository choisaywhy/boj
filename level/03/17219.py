import sys

def solution(N,M,pswd,search):
    for site in search :
        print(pswd[site])





if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    pswd = {}
    for _ in range(N) :
        site, pw = map(str, input().strip().split())
        pswd[site] = pw
    search = [str(input().strip()) for _ in range(M)]
    solution(N,M,pswd,search)