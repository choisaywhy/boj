import sys

def solution(a,b):
    print(a+b,a-b,a*b,a//b,a%b,sep="\n")





if __name__ == "__main__" :
    input = sys.stdin.readline
    a,b = map(int,input().split())
    solution(a,b)