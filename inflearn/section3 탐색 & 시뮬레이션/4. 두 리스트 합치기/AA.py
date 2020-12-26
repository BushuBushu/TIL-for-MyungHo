import sys
sys.stdin = open("data/in1.txt", "rt")

N = int(sys.stdin.readline())
n = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))

# 내 풀이
num = m+n
num.sort()
for x in num :
    print(x, end = ' ')

# 강의 풀이
c = []
p1 = p2 = 0

while p1<N and p2<M : #point 변수가 배열 끝까지 가면 끝난다.
    if n[p1] <= m[p2] :
        c.append(n[p1])
        p1 += 1
    else :
        c.append(m[p2])
        p2 += 1
if p1 < N : # p1이 N보다 작다 == p1의 수가 끝까지 못 가고 남았다.
    c = c + n[p1:]
if p1 < M : 
    c = c + m[p2:]
    
for x in c :
    print(x, end = ' ')
