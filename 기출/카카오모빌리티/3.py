import sys

input = sys.stdin.readline

def solution(s, times):
    daily = 1 # 1일 1저축
    days = 0 # 저축 기간 

    d = 0
    h, m, s = map(int, s[11:].split(":"))

    for time in times :
        td, th, tm, ts = map(int, time.split(":"))
        d += td
        h += th
        m += tm
        s += ts

        if s >= 60 :
            s -= 60
            m += 1
        if m >= 60 :
            m -= 60
            h += 1
        if h >= 24 :
            h -= 24
            d += 1
        
        if d > 1 :
            daily = 0
        days += d
        d = 0
    
    return [daily, days+1]

times2 = ["01:06:30:00", "01:01:12:00",
          "99:00:09:25", "99:00:09:25", "99:00:09:25", "99:00:09:25", "99:00:09:25"]
s = "2021:12:29:16:08:35"
print(solution(s, times2))