import sys

def solution(S):
    
    count0 = 0
    count1 = 0

    prev = S[0]

    for s in S :
        if s != prev :
            if prev == "0" :
                count0 += 1
            elif prev == "1" :
                count1 += 1
        prev = s
    

    # s[-1]직전 까지 밖에 탐색을 못하므로, 마지막 노드 탐색 필수
    if S[-1] == '0' :
        count0 += 1
    else :
        count1 += 1

    print(min(count0, count1))


if __name__ == "__main__" :
    input = sys.stdin.readline
    S = str(input()).strip()
    solution(S)