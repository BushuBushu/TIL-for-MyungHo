import sys

sys.stdin = open("data/in1.txt", "rt")
N = sys.stdin.readline() # kdk1k0kdjfkj0kkdjkfj0fkd
res = 0

print(N)
for x in N :
    if x.isdecimal() : # x가 0 ~ 9의 숫자일 때 True
        res = res * 10 + int(x) # 정수로 저장되기 때문에 앞의 0이 사라짐
print(res)

cnt = 0
for i in range(1, res +1) : # 약수 찾기
    if res % i == 0:
        cnt += 1
print(cnt)
