import sys

sys.stdin = open("data/in6.txt", "rt")
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
print(a)

# 0 ~ 9 까지 3개로 나누기
def Count(len) :
    cnt = 0
    num = 0
    
    for i, x in enumerate(a) :
        num += x
        if i < rt :
            if num == sum(a[lt:len])  :
                num = 0
                cnt += 1
                print(sum(a[lt:len]))
                print(num)
            elif num + a[i+1] > sum(a[lt:len])  :
                num = 0
                cnt += 1
                print(num)
    if num >= 1 :
        cnt += 1

    return cnt

lt = 1
rt = sum(a)
while lt <= rt :
    mid  = (lt + rt) // 2
    if Count(mid) >= M :
        res =+ 1
    else :
        res -= 1
