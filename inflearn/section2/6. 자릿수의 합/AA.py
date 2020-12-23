import sys
sys.stdin = open("data/in1.txt", "rt")

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
num = 0

#내 풀이
def  digit_sum(arr) :
    numMax = -214700000 #가장 큰 값을 구하기 위한 변수
    index = 0 # 원래 값을 구하기 위한 index를 저장하는 변수
    for i, x in enumerate(arr):
        num = str(x) # 문자열로 형변환을 해주어야 for문에 사용 가능
        sum = 0
        for j, y in enumerate(num) :
            sum += int(y)
        if sum > numMax :
            numMax = sum
            index = i
    print(arr[index])    

digit_sum(arr)

# 강의 풀이1 (바로 처리하는 방법)

def digit_sum(x) :
    sum = 0
    while x > 0 : #x가 125일 때
        sum += x%10 #5 2 1
        print(sum)
        x = x // 10 # 12 1 0
    return sum

max = -214700000
for x in arr :
    tot = digit_sum(x)
    if tot > max :
        max = tot
        res = x
        
print(res)

# 강의 풀이2 (str 처리)

def  digit_sum(x) :
    sum = 0
    for i in str(x) :
        sum += int(i)
    return sum

max = -214700000
for x in arr :
    tot = digit_sum(x)
    if tot > max :
        max = tot
        res = x
        
print(res)