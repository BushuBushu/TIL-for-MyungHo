## 격자판 최대합

#### 내 풀이

```python
#input
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
output
155
```

**초기 변수**

```python
diagonal_right= 0 #좌 -> 우 대각선
diagonal_left = 0 # 우 -> 좌 대각선
vertical_list = [0] * N #세로 값 저장 리스트
vertical_max = -2400000 #세로
horizontal = 0 #가로값 저장 변수
horizontal_max = -2400000 #가로
```

##### 반복문 내에서 가로, 대각선, 세로 값 구하기

```python
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
```

##### 리스트에 저장되어 있는 세로 값만 따로 구하기

`````python
print(vertical_list[j]) # [532, 371, 253, 438, 525, 611, 435, 409, 508, 514]
for x in vertical_list :
    if x > vertical_max :
         vertical_max = x
`````

##### 가로 세로 대각선 중에서 가장 큰 값 찾기

```python
num_list = [diagonal_right,diagonal_left,vertical_max,horizontal_max] #최종 값 리스트
num_max = -2400000
for x in num_list :
    if x > num_max :
        num_max = x
print(num_max)
```



##### 강의 풀이

#####  초기 변수

`````python
a = [list(map(int, input().split())) for _ in range(N)] #input 한 줄을 읽어서 리스트화 시킴 * N번
#a가 2차원 배열로 저장 됨
[[10 13 10 12 15]
[12 39 30 23 11]
[11 25 50 53 15]
[19 27 29 37 27]
[19 13 30 13 19]]
largest = -2147000000 #최댓값
`````

##### 가로 세로 최댓값 구하기

`````python
for i in range(N) :
    sum1 = sum2 = 0
    for j in range(N) :
        #첫 i는 [10 13 10 12 15] [..]..
        #두번째 i는 10, 13, 10...를 나타냄
        sum1 += a[i][j] #가로의 합
        sum2 += a[j][i] # 세로의 합
        
    if sum1 > largest :
        largest = sum1
    if sum2 > largest :
        largest = sum2
`````

##### 대각선 최댓값 구하기

`````python
[10 13 10 12 15]for i in range(N) :
    sum1 += a[i][i] #좌 -> 우 대각선 합
    #i = [10 13 10 12 15]
    #[N-i-1] = 15 , -인덱스는 0이 아닌 -1부터 시작
    sum2 += a[i][N-i-1] # 우 -> 좌 대각선 합
    
if sum1 > largest :
    largest = sum1
if sum2 > largest :
    largest = sum2
`````

##### 최댓값

`````python
print(largest)
`````



#### 후기

* 다음 2차원 리스트 문제에서는 **2차원 리스트**를 고려해서 풀어봐야겠다.