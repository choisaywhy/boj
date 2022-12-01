import sys

N = int(sys.stdin.readline())

for _ in range(N):
    A,B = map(int, sys.stdin.readline().split())
    lcm = A*B
    while B >0:
        A, B = B, A % B
    lcm //= A
    print(lcm)