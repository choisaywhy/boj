def solution(flowers):
    answer = []
    
    for days in flowers :
        start, end = days
        for d in range(start, end) :
            answer.append(d)
    

    return len(set(answer))