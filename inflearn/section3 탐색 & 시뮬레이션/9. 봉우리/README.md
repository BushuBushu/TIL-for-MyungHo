## 봉우리

#### 내 풀이

##### 초기 변수

```python
#input
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2
#output
10

N = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
```

##### 요구사항의 리스트 추가

```python
a.insert(0,[0] * N) #a[0] 앞에 리스트 추가
a.append([0] * N) # a[N]번째 뒤에 리스트 추가
for i in range(len(a)) :
    #a 리스트 맨 앞과 뒤에 0 삽입
    a[i].insert(0, 0)
    a[i].append(0)
    
0 0 0 0 0 0 0    
0 5 3 7 2 3 0
0 3 7 1 6 1 0
0 7 2 5 3 4 0
0 4 3 6 4 1 0
0 8 7 3 5 2 0
0 0 0 0 0 0 0
```

##### 상하 좌우 크기 비교

> range(1, N + 1) 시작하는 이유는 맨 위와 맨 아래는 0이기 때문
>
> and 연산자를 이용해서 `a[i][j]`상하좌우 보다 클 때 count가 되도록 설계

```python
cnt = 0
for i in range(1, N + 1) :
    for j in range(1, N + 1) : #상하좌우
        if a[i][j] > a[i-1][j] and a[i][j] > a[i+1][j] and a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1]  :
            cnt += 1
            
print(cnt)
```



#### 강의 풀이

##### 초기변수

* 위와 같음

##### 상하좌우 리스트 생성

> 상하좌우를 탐색할 때는 list를 만들어준다.
>
> dx는 i (행)를 나타내며 **-1은 상**을, **1은 하**를 나타낸다
>
> dy는 j (열)를 나타내며 **1은 우**을, **-1은 좌**를 나타낸다

```python
#상우하좌
dx = [-1, 0, 1, 0] # 행 i 
dy = [0, 1, 0, -1] # 열 j
```

##### 상하좌우 크기 비교

> 여기서 내장함수 **all**을 사용했는데 all안의 요소가 참이면 True를 반환한다.

```python
# for문을 사용해서 k를 통해 상하좌우를 탐색할 수 있도록 했다.
a[i + dx[k]][j+dy[k]] for k in range(4)
a[i - 1][j + 0] #상
a[i + 0][j + 1] #우
a[i + 1][j + 0] #하
a[i + 0][j - 1] #좌
```



```python
cnt = 0
for i in range(1, N + 1) :
    for j in range(1, N + 1) :
        if all(a[i][j] > a[i + dx[k]][j+dy[k]] for k in range(4)) :
            cnt += 1
            
print(cnt)
```



#### 후기

다음에 상하좌우를 탐색할 때는 리스트를 만들어서 풀어봐야겠다.