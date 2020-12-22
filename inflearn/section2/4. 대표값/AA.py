import sys
import math
sys.stdin = open("data/in3.txt", "rt")

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ave = math.floor((sum(arr)/N) + 0.5) #round 사용 x
arrMin = float('inf')

'''
for i in range(len(arr)):
    tmp = abs(arr[i] - ave)
    if tmp < arrMin :
        arrMin = tmp
        index = i + 1

    elif tmp == arrMin :
        if arr[index] < arr[i] :
            arrMin = tmp
            index = i + 1
            
print("%d %d" %(ave, index))
'''

for idx, x in enumerate(arr) : #emumerate : idx, x를 같이 사용할 수 있다.
    tmp = abs(x - ave) #tmp가 가장 작은 학생이 평균과 가깝다
    if tmp < arrMin :
        arrMin = tmp 
        score = x #해당 학생 점수
        index = idx+1
    elif tmp == arrMin :
        if score < x :
            score = x
            index = index +1

print("%d %d" %(ave, index))
