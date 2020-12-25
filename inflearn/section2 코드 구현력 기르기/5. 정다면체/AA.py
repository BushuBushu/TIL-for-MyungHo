import sys
sys.stdin = open("data/in1.txt", "rt")

N, M =  map(int, sys.stdin.readline().split())

a = list(range(1, N +1))
b = list(range(1, M +1))
count= [0] * (N + M +3) #배열에 0값으로 채워 넣기
arrMax = 0 # 가장 큰 값 넣을 변수

#내 풀이
for i, x in enumerate(a):
    for j, y in enumerate(b) :
        add = x + y # 두 수의 합
        count[add -1] += 1 # 두 수의 합 카운팅

for i, z in enumerate(count):
    if max(count) == count[i] : # 가장 큰 카운팅 값과 같은 조건 
        print(i + 1, end =" ")


#강의 풀이
for i in range(1, N +1) :
    for j in range(1, M +1) :
        count [i+j] += 1

for i in range(N + M + 1):
    if count[i] > arrMax:
        arrMax = count[i] #가장 큰 값 저장

for i in range(N + M + 1):
    if count[i] == arrMax : #가장 큰 값과 카운팅 값이 같은 조건
        print(i, end=' ')
