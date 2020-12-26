import sys

sys.stdin = open("data/in1.txt", "rt")

#내풀이
arr = list(range(1, 21)) # 1 부터 20까지의 배열 생성
for i,x in enumerate(range(10)) : # 10번의 반복
    a, b = map(int, sys.stdin.readline().split())# 5, 10 ...
    arr_reverse = arr[a-1:b] # index arr[4] =5부터 arr[10] =9 전까지 5,6,7,8,9
    arr_reverse.reverse() # 9 8 7 6 5
    arr[a-1:b] =  arr_reverse # 해당 리스트 반전

for i, x in enumerate(arr) :
    print(arr[i], end = ' ')

# 강의 풀이
a = list(range(21)) # 0 부터 20까지의 배열 생성
for _ in range(10) : # _ 변수의 값이 필요 없을 때
    s, e = map(int, sys.stdin.readline().split())# 5, 10 ...
    for i in range((e-s+1)//2) : #(10-5+1)//2 = 3 
        # i = 0,1,2
        a[s+i], a[e-i] = a[e-i], a[s+i] #5,10=10,5 6,9=9,6...
a.pop(0)
for x in a : 
    print(x,end = ' ')
