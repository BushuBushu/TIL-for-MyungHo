import sys
sys.stdin = open("data/in1.txt", "rt")
N = int(sys.stdin.readline())


#내 풀이
diagonal_right= 0 #좌 -> 우 대각선
diagonal_left = 0 # 우 -> 좌 대각선
vertical_list = [0] * N #세로 값 저장 리스트
vertical_max = -2400000 #세로
horizontal = 0  #가로값 저장 변수
horizontal_max = -2400000 #가로

for i in range(N) :
    arr = list(map(int, sys.stdin.readline().split()))
    
    # 가로 최대값
    horizontal = sum(arr)
    if horizontal > horizontal_max :
        horizontal_max = horizontal

    #좌 -> 우 대각선 값
    diagonal_right += arr[i]

    #우 -> 좌 대각선 값
    diagonal_left += arr[-i -1]

    # 세로 값 저장 리스트
    for j in range(N) :
        vertical_list[j] += arr[j] # list에 변하는 arr를 계속해서 더하기

#세로 최대값
for x in vertical_list :
    if x > vertical_max :
         vertical_max = x

num_list = [diagonal_right,diagonal_left,vertical_max,horizontal_max] #최종 값 리스트
num_max = -2400000
for x in num_list :
    if x > num_max :
        num_max = x
print(num_max)


# 강의 풀이
a = [list(map(int, input().split())) for _ in range(N)] #input 한 줄을 읽어서 리스트화 시킴 * N번
largest = -2147000000
for i in range(N) :
    sum1 = sum2 = 0
    for j in range(N) :
        sum1 += a[i][j] #가로의 합
        sum2 += a[j][i] # 세로의 합
        
    if sum1 > largest :
        largest = sum1
    if sum2 > largest :
        largest = sum2
sum1 = sum2 = 0
for i in range(N) :
    sum1 += a[i][i] #좌 -> 우 대각선 합
    sum2 += a[i][N-i-1] # 우 -> 좌 대각선 합
    
if sum1 > largest :
    largest = sum1
if sum2 > largest :
    largest = sum2

print(largest)
    
