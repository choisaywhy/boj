import sys

def solution(N,M,dictbynum,dictbyname,questions):
    for q in questions :
        if q.isnumeric() :
            print(dictbynum[int(q)])
        else :
            print(dictbyname[q])
    return



if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    dictbynum = {}
    dictbyname = {}
    for i in range(1,N+1) :
        name = str(input().strip())
        dictbynum[i] = name
        dictbyname[name] = i
    questions = [str(input().strip()) for _ in range(M)]

    solution(N,M,dictbynum,dictbyname,questions)