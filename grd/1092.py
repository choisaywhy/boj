import sys
def solution():
    n = int(input())
    crain = list(map(int,input().split()))
    m = int(input())
    boxes = list(map(int,input().split()))
    boxes.sort(reverse=True)
    crain.sort(reverse=True)

    if boxes[0] > crain[0]:
        return -1
    
    mins = 0
    count = 0
    moved = [False]*m

    while count < m:
        for c in crain:
            for i in range(m):
                if moved[i] or boxes[i] > c:
                    continue
                moved[i] = True
                count += 1
                break
        mins += 1

    return mins

    

if __name__ == "__main__" :
    input = sys.stdin.readline

    print(solution())