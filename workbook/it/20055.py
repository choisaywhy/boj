import sys
from collections import deque

def solution(N, K, A, index):
    zeros = A.count(0) # 내구도 0 개수 파악
    step = 1 # 진행 단계
    robots = deque([False]*(2*N)) # 로봇 위치 Index (index와 동기화)
    
    while True:
        #1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다 (내구도 감소 없음)
        index.appendleft(index.pop()) # 2n을 1로
        robots.appendleft(robots.pop()) 
        if robots[N-1]:
            robots[N-1] = False
        

        #2. 가장 먼저 벨트에 올라간 로봇부터(N부터 역순으로), 한 칸씩 이동한다 (내구도 감소)
        for i in range(N-2, -1, -1): # 0 ~ N-1 역순
            if not robots[i] or robots[i+1] or A[index[i+1]] == 0: # 해당 칸에 로봇이 없거나, 움직일 수 없는 칸이면
                continue
            robots[i+1], robots[i] = True if i+1 != N-1 else False, False
            
            A[index[i+1]] -= 1
            if A[index[i+1]] == 0:
                zeros += 1
        
        #3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇을 올린다 (내구도 감소)
        if A[index[0]] > 0 and not robots[0]:
            robots[0] = True
            A[index[0]] -= 1
            if A[index[0]] == 0:
                zeros += 1

        # debugging
        # print('step',step)
        # print(list(A[i] for i in index))
        # print(robots)

        #4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다
        if zeros >= K:
            break

        step += 1

    print(step)


if __name__ == "__main__" :
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    index = deque([i for i in range(0, 2*N)])
    solution(N, K, A, index)