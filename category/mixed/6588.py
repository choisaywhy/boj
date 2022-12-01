import sys


def is_primary(N:int):
    primary = [True] * (N + 1)
    primary[0], primary[1] = False, False

    for i in range(2, N+1):
        if primary[i] :
            j = 2
            while i*j <= N:
                primary[i*j] = False
                j += 1

    return primary


array = []
while True:
    num = int(sys.stdin.readline())
    if not num :
        break
    array.append(num)


primary = is_primary(max(array))

for num in array :
    result = None
    for i in range(3,int(num/2)+1):
        if primary[i] and primary[num-i]:
            result = f'{num} = {i} + {num-i}'
            break
    if result :
        print(result)
    else :
        print("Goldbach's conjecture is wrong.")