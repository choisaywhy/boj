import sys

def solution(N,K,plug):
    multi_tap = []
    count = 0

    for i in range(K) :
        if plug[i] in multi_tap :
            continue
        if len(multi_tap) < N :
            multi_tap.append(plug[i])
            continue
        
        if i < K - N :
            new_tap = 0
            new_index = 0
            new_plug = plug[i+1:]
            for j in range(N) :
                if multi_tap[j] not in new_plug :
                    new_index = j
                    break        
                if new_plug.index(multi_tap[j]) > new_tap :
                    new_tap = new_plug.index(multi_tap[j])
                    new_index = j

            multi_tap[new_index] = plug[i]
        count += 1
    print(count)




if __name__ == "__main__" :
    input = sys.stdin.readline
    N, K = map(int,input().split())
    plug = list(map(int,input().split()))
    solution(N,K,plug)