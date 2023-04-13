import sys

def solution(t):
    t.sort()

    if t[0]+t[1] <= t[2]:
        print("Invalid")
        return
    if t[0] == t[1] == t[2]:
        print("Equilateral")
        return
    if t[0] == t[1] or t[1] == t[2]:
        print("Isosceles")
        return
    print("Scalene")
    return






if __name__ == "__main__" :
    input = sys.stdin.readline
    t = list(map(int, input().split()))
    while t != [0,0,0]:
        solution(t)
        t = list(map(int, input().split()))
