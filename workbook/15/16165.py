import sys

def solution(N, M, group, member):
    
    for _ in range(M):
        quiz = input().strip()
        types = int(input())

        if types == 1:
            print(member[quiz])
        else:
            for mem in sorted(group[quiz]):
                print(mem)



if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    group = {}
    member = {}
    
    for _ in range(N):
        group_name = input().strip()
        num = int(input())
        group[group_name] = []

        for _ in range(num):
            member_name = input().strip()
            group[group_name].append(member_name)
            member[member_name] = group_name
    solution(N, M, group, member) 