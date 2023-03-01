import sys

def solution(K, L):
    system = {}
    log = []

    for i in range(L) :
        student = str(input().strip())
        
        system[student] = i
        log.append(student)

    
    count = 0
    for i in range(L) :
        
        if count == K :
            break

        if i != system[log[i]] :
            continue
        print(log[i])
        count += 1



if __name__ == "__main__" :
    input = sys.stdin.readline
    K, L = map(int, input().split())
    solution(K, L)