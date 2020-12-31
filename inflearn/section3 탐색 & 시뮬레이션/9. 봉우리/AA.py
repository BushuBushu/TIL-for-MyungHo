import sys
sys.stdin = open("data/in1.txt", "rt")

N = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#내 풀이
a.insert(0,[0] * N) #a[0] 앞에 리스트 추가
a.append([0] * N) # a[N]번째 뒤에 리스트 추가
for i in range(len(a)) :
    a[i].insert(0, 0)
    a[i].append(0)

cnt = 0
for i in range(1, N + 1) :
    for j in range(1, N + 1) : #상하좌우
        if a[i][j] > a[i-1][j] and a[i][j] > a[i+1][j] and a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1]  :
            cnt += 1
            
print(cnt)

# 강의 풀이
a.insert(0,[0] * N) #a[0] 앞에 리스트 추가
a.append([0] * N) # a[N]번째 뒤에 리스트 추가
for i in range(len(a)) :
    a[i].insert(0, 0)
    a[i].append(0)

#상우하좌
dx = [-1, 0, 1, 0] # 행 i 
dy = [0, 1, 0, -1] # 열 j
cnt = 0
for i in range(1, N + 1) :
    for j in range(1, N + 1) : #상하좌우
        # all은 x요소가 모두 참이면 True 반
        if all(a[i][j] > a[i + dx[k]][j+dy[k]] for k in range(4)) :
            cnt += 1
            
print(cnt)
