import sys

def solution(N,M,K,power,cable):
    parents = [i for i in range(N+1)]
    cost = 0

    def find(u):
        if parents[u] != u:
            parents[u] = find(parents[u])
        return parents[u]

    def union(u,v): # pu,pv가 다르다는걸 전제함
        pu = find(u)
        pv = find(v)
        if pu in power and pv in power:
            return False
        if pu in power:
            parents[pv] = pu
        elif pv in power:
            parents[pu] = pv
        else:
            parents[max(pv,pu)]=min(pu,pv)
        return True

    for w,u,v in cable:
        flag = False
        if find(u) == find(v) : # 이미 연결됨
            continue
        
        if union(u,v):
            cost += w


        for i in range(1,N+1):
            if find(i) not in power:
                flag = True
                break

        if not flag:
            break


    print(cost)


if __name__ == "__main__" :
    input = sys.stdin.readline
    N,M,K = map(int,input().split()) # 도시 개수, 케이블 개수, 발전소 개수
    power = list(map(int, input().split()))
    cable = []
    for _ in range(M):
        u,v,w = map(int, input().split())
        cable.append((w,u,v))
    cable.sort()
    solution(N,M,K,power,cable)



# import sys

# def solution(N,M,K,power,cable):
#     parents = [i for i in range(N+1)]
#     cost = 0

#     def find(u):
#         if parents[u] != u:
#             parents[u] = find(parents[u])
#         return parents[u]

#     def union(u,v): # pu,pv가 다르다는걸 전제함
#         pu = find(u)
#         pv = find(v)
#         if pu in power and pv in power:
#             return False
#         if pu in power:
#             parents[pv] = pu
#         elif pv in power:
#             parents[pu] = pv
#         else:
#             parents[max(pv,pu)]=min(pu,pv)
#         return True

#     for w,u,v in cable:
#         flag = False
#         if find(u) == find(v) : # 이미 연결됨
#             continue
        
#         if union(u,v):
#             cost += w

#         print(w,u,v,'성사')
#         print(parents)
#         print(cost,'cost 갱신')

#         for i in range(1,N+1):
#             if find(i) not in power:
#                 flag = True
#                 break

#         if not flag:
#             break


#     print(cost)
#     print(parents)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N,M,K = map(int,input().split()) # 도시 개수, 케이블 개수, 발전소 개수
#     power = list(map(int, input().split()))
#     cable = []
#     for _ in range(M):
#         u,v,w = map(int, input().split())
#         cable.append((w,u,v))
#     cable.sort()
#     solution(N,M,K,power,cable)