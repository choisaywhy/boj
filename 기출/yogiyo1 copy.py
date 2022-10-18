import sys
import datetime as dt

input = sys.stdin.readline
# 1
def solution(S):
    order = {}
    for _ in range(len(S)):
        photo, city, time = map(str, input().strip().split(','))
        order[city] = order.get(city, []) + [(photo, time)]
    
    