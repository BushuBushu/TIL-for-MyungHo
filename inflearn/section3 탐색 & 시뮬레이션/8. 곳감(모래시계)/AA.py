import sys
sys.stdin = open("data/in1.txt", "rt")

N = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M = int(sys.stdin.readline())

#회전 코드
for i in range(M) :
    b = list(map(int, sys.stdin.readline().split()))
    arr = [0] * N #빈 배열 생성

    #오른쪽 회전    
    if b[1] == 1 :
        p1 = b[2] # 오른쪽 index 증가
        p2 = 0 # 왼쪽 index 증가

        while N < p2 : # p2가 N 보다 크면 N 만큼 계속 뺴준다.
            p2 = p2 - N
        
        for j in range(N) :
            if N - p1 > 0 :
                #ex ) 0,0,82,38,20,16,42
                arr[p1] = a[b[0] -1][j]
                p1 += 1
            else :
                #ex) 1,79 + 82,38,20,16,42
                arr[p2] = a[b[0] -1][j]
                p2 += 1
                
        a[b[0] - 1] = arr #해당하는 리스트에 arr를 삽입해준다.
    #왼쪽 회전
    else :
        p2 = b[2] # 왼쪽 index 증가
        p1 = 0   # 오른쪽 index 증가
        
        while N < p2 : # p2가 N 보다 크면 N 만큼 계속 뺴준다.
            p2 = p2 - N
            
        for j in range(N-1, -1, -1) : # 6,5,4,3,2,1,0
            if N - p2 > 0 :
                print(a[b[0]-1])
                print(arr)
                arr[N - p2 -1] = a[b[0] -1][j]
                p2 += 1
            else :
                arr[N - p1 -1] = a[b[0] -1][j] 
                p1 += 1
        a[b[0] - 1] = arr

# 합 구하기
center = N // 2 #3 중간 값 0,1,2,3,4,5,6,7
p1 = 0
p2 = N
num = 0
for i in range(N) :
    if i < center : #0,1,2 < 3
        for j in range(p1, p2) :
            num += a[i][j]
        p1 += 1
        p2 -= 1 
    else : 
        for j in range(p1, p2) : #중간 값부터 시작
            num += a[i][j]
        p1 -= 1
        p2 += 1
print(num)


# 강의 풀이
# 회전 하기
for i in range(M) :
    h, t, k = map(int, input().split())
    #왼쪽으로 회전
    if t == 0 :
        for _ in range(k) :
            #제일 앞에 있는 값을 빼 내서 리스트 맨 뒤로 저장
            # 빠진 수 자리를 다음 수가 index 0으로 채움
            a[h - 1].append(a[h - 1].pop(0))

    # 오른쪽으로 회전
    else :
        for _ in range(k) :
            a[h - 1].insert(0, a[h - 1].pop()) #제일 뒤에 있는 값을 빼 내서 리스트 맨 앞으로 저장

# 합 구하기
p1 = 0
p2 = N - 1
num = 0
for i in range(N) :
        for j in range(p1, p2 + 1) :
            num += a[i][j]
        if i < N // 2 :
            p1 += 1
            p2 -= 1
        else :
            p1 -= 1
            p2 += 1
print(num)
