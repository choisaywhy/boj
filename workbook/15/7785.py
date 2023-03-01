import sys

def solution(n):
    log = {}

    for _ in range(n) :
        name, state = map(str, input().strip().split())
        if state == 'enter' :
            log[name] = 'enter'
        else :
            del(log[name])

    for name in sorted(list(log.keys()), reverse = True) :
        print(name)


if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    solution(n)