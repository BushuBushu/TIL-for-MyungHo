import sys
sys.stdin = open("data/in1.txt", "rt")

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#내 풀이
center = int(N // 2) # 0,1,2,3,4,5,6 의 중간 값은 3
tot = arr[0][center] # 다이이아 몬드의 맨 위 중간 값 + 최종 누적 값
p1 = center #좌로 이동할 인덱스 위치
p2 = center #우로 이동할 인덱스 위치
for i in range(1,N) :
    if i <= center : #다이아 몬드 중간 윗부분
        p1 -= 1 #2 1 0
        p2 +=  1 #4 5 6
        tot += sum(arr[i][p1:p2 +1])
    else : #다이아몬드 중간 아랫부분
        p1 +=  1 #1 2
        p2 -= 1 #5 4
        tot += sum(arr[i][p1:p2 +1])
    
print(tot)

# 강의 풀
res = 0 #누적 값
s =e = N//2 # 다이아몬드 중간 값
for i in range(N) :
    for j in range(s, e +1) : #s 값부터 e 값까지만 반복
        res += arr[i][j]
    if i < N//2 :
        s -= 1
        e += 1
    else :
        s += 1
        e -= 1
print(res)
