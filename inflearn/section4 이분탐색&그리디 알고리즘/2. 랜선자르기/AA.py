import sys
import math

sys.stdin = open("data/in3.txt", "rt")
K, N = map(int, sys.stdin.readline().split())
'''
# 내 풀이 5번 input Time Limit Exceeded ...
num = 0
a = []
for i in range(K) : 
    b = int(sys.stdin.readline())
    a.append(b)
    num += b
num = (num / N)
num = math.ceil(num)
stop = True
while stop :
    ch = 0
    for i in range(K) :
        if ch != N :
            ch += a[i] // num
        elif ch == N :
            print(num)
            stop = False
            break
    if ch > N :
        print(num)
        break
    num -= 1
'''
# 강의 풀이
def Count(len) :
    cnt = 0
    for x in Line :
        cnt += (x // len) #ex) 802 에서 401로 몇 개를 만들 수 있는지
    return cnt

Line = []
res = 0 # 최댓값
largest = 0 # 리스트에서 가장 큰 값
for i in range(K) : 
    tmp = int(sys.stdin.readline())
    Line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest
while lt <= rt :
    mid = (lt + rt) //2 # 동일한 랜선의 길이
    if Count(mid) >= N :
        res = mid
        lt = mid +1
    else :  #길이가 너무 길다
        rt = mid - 1
print(lt, rt)
print(res)       
