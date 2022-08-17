import sys


A,B = map(int, sys.stdin.readline().split())
gcd = 0
lcm = A * B

while B >0:
    A, B = B, A % B
gcd = A
lcm //= gcd

print(gcd,lcm,sep='\n')