import sys
#sys.stdin = open("data/in6.txt", "rt")
N = int(sys.stdin.readline())

# 내풀이 (Time Limit Exceeded 에러가 남)
arr = list(range(1, N + 1))
cnt = [0] * (N +3)
num = 0
'''for i, x in enumerate(arr):
    for j, y in enumerate(arr) :
        if x % (j + 1) == 0 :
            cnt[i] += 1
for i, x in enumerate(cnt) :
    if x == 2 :
        num += 1
print(num)'''

# 강의 풀이 (에라토스테네스 체 방법 사용)
ch = [0] * (N +3)
cnt = 0 # 소수가 몇 개인지
for i in range(2, N+1): #1은 소수가 아니기 때문에 2부터 시작
    if ch[i] == 0 : #ch[0]가 0이면 소수
        cnt += 1
        for j in range(i, N +1, i): #i의 배수 만큼 증가
            ch[j] = 1
            
print(cnt)
