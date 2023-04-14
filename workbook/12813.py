import sys

def solution(A, B):
    andop, orop, xorop, notA, notB = '','','','',''
    for a, b in zip(A, B):
        andop += str(a and b)
        orop += str(a or b)
        xorop += str(a ^ b)
        notA += str(0 if a else 1)
        notB += str(0 if b else 1)
    
    print(andop)
    print(orop)
    print(xorop)
    print(notA)
    print(notB)






if __name__ == "__main__" :
    input = sys.stdin.readline
    A = map(int,input().strip())
    B = map(int,input().strip())
    solution(A, B)