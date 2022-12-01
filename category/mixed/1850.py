import sys

A,B = map(int, sys.stdin.readline().split())

while B >0:
    A, B = B, A % B
print("1"*A)