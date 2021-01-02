import sys
sys.stdin = open("data/in1.txt", "rt")
a = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]
'''
# 내풀이
cnt = 0
for i in range(7) :
    ch1 = [] #행 값 저장
    ch2 = [] #열 값 저장
    for j in range(7) :
        ch1.append(a[i][j])
        ch2.append(a[j][i])
    
    for j in range(3) :
        ch1_sm = ch1[0+j:5+j]
        ch2_sm = ch2[0+j:5+j]
        if ch1_sm == ch1_sm[::-1] :
            cnt += 1
        if ch2_sm == ch2_sm[::-1] :
            cnt += 1
         
print(cnt)
'''
# 강의 풀이

cnt = 0
for i in range(3) :
    for j in range(7) :
        #행 조회
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1] :
            cnt += 1
        #열 조회
        for k in range(2) :
            if a[i+k][j] != a[i+5-k-1][j] :
                break
        else:
            cnt += 1
print(cnt)
