import sys

def solution(N, flower):
    
    flower.sort(key = lambda x : [x[0], x[1]])
    count = 0
    sm, sd = 3, 1
    em, ed = 0, 0
    for f in flower :

        bm, bd, fm, fd = f

        if (sm, sd) < (bm, bd):
            count += 1
            sm, sd = em, ed
            em, ed = 0, 0


        if (sm, sd) >= (bm, bd) :
            if (em, ed) < (fm, fd) :
                em, ed = fm, fd

        if (sm, sd) > (11, 30) :
            break
        if (em, ed) > (11, 30) :
            count += 1
            break
    
    if (em, ed) > (11, 30) :
        print(count)
    else :
        print(0)




if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    flower = []
    for _ in range(N) :
        flower.append(list(map(int, input().split())))
    solution(N, flower)


# debugging
# import sys

# def solution(N, flower):
    
#     flower.sort(key = lambda x : [x[0], x[1]])
#     count = 0
#     sm, sd = 3, 1
#     em, ed = 0, 0
#     print(flower)
#     for f in flower :
#         print(f,'turn')

#         bm, bd, fm, fd = f

#         if (sm, sd) < (bm, bd):
#             print('outof range')
#             count += 1
#             sm, sd = em, ed
#             em, ed = 0, 0
#             print(sm,sd,'시작점 갱신')
#             print(count, 'count 갱신')


#         if (sm, sd) >= (bm, bd) :
#             print(sm,'/',sd,'보다 더 일찍 핌',bm, bd)
#             if (em, ed) < (fm, fd) :
#                 em, ed = fm, fd
#                 print(em,ed,'끝나는 최댓날 갱신')

#         if (sm, sd) > (11, 30) :
#             break
#         if (em, ed) > (11, 30) :
#             count += 1
#             break
    
#     if (em, ed) > (11, 30) :
#         print(count)
#     else :
#         print(0)




# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     flower = []
#     for _ in range(N) :
#         flower.append(list(map(int, input().split())))
#     solution(N, flower)

