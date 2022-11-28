import sys

def solution(N,M,arr) :
    def DFS(index, res):
        if len(res) == M : # 백트래킹, 길이를 만족하면 result 추가 후 return
            result.append(res)
            return
        
        for i in range(N) : 
            if index == i : # 같은 index 무시 (중복 제거)
                continue
            DFS(i ,res + arr[i]) # res 업데이트 하여 재귀

    result = []
    DFS(N+1, "")

    # 중복 제거하여 사전순 출력
    for re in sorted(list(set(result))) :
        for r in re :
            print(r, end=" ")
        print()


if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = sorted(list(map(str, input().split()))) # 사전 순으로 arr 할당
    solution(N,M,arr)