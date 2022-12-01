def solution(id_list, k):
    total = {}

    for ids in id_list :
        ids = set(ids.split())

        for i in ids :
            total[i] = total.get(i, 0) + 1
            if total[i] > k :
                total[i] -= 1
    
    answer = sum(total.values())

    return answer