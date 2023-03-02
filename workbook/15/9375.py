import sys

def solution(n, clothes):
    ans = 1
    for cloth in clothes :
        ans *= (clothes[cloth] + 1)
    
    print(ans-1)



if __name__ == "__main__" :
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T) :
        clothes = {}
        n = int(input())
        for _ in range(n) :
            name, cloth = map(str, input().strip().split())
            clothes[cloth] = clothes.get(cloth, 0) + 1
        
        solution(n, clothes)