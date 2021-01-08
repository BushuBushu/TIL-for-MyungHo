## 랜선자르기 (결정알고리즘)

#### 내 풀이 (강의 풀이를 참고하는게 좋다)

##### 초기 변수

```python
#input
4 11
802
743
457
539
#output
200

K, N = map(int, sys.stdin.readline().split())
num = 0
a = []
```

##### 기준 값 구하기

* 모든 수를 더하고 N만큼 나누어 준다. 나온 값을 올림해준다.

* ```python
  for i in range(K) : 
      b = int(sys.stdin.readline())
      a.append(b)
      num += b
  num = (num / N)
  num = math.ceil(num) #231
  ```

* 이렇게 하는 이유는  num에서 output 값인 200이 나올 때까지 231에 -1을 누적해준다.

##### 값 구하기

* ```python
  802 // N 
  743 // N
  457 // N
  539 // N
  #일 때 나온 몫을  ch에 저장한다.
  #ch가 N과 같아지면 while문을 나온다.
  ```

```python
stop = True #if문에서 break할 때 while 문도 멈추기 위한 변수
while stop :
    ch = 0 #a[i] 값들을 N으로 나눈 몫을 누적하는 변수
    for i in range(K) :
        if ch != N :
            ch += a[i] // num
        elif ch == N :
            print(num)
            stop = False
            break
    if ch > N : #ch가 N값을 넘어가게 되면 break
        print(num)
        break
    num -= 1 # 231 -> 200 될 때까지 -1
```



#### 강의 풀이

##### 이분검색을 사용

```python
#input
4 11
802
743
457
539
#output
200

1 ~ 802
1 ~ 401
1 ~ 200
100을 변수에 넣어서 100 ~ 200 사이에서 값을 찾을 수 있다,

802 // 100 #6
743 // 100 #5
457 // 100 #3
539 // 100 #4
#값은 18이 나오는데 N보다 크다 
```

##### 초기 변수

* 이분 검색을 사용하기 위해 lt , rt 변수를 지정해준다.

```python
K, N = map(int, sys.stdin.readline().split())
Line = []
res = 0 # 최댓값
largest = 0 # 리스트에서 가장 큰 값
for i in range(K) : 
    tmp = int(sys.stdin.readline())
    Line.append(tmp)
    largest = max(largest, tmp)#tmp 중 가장 큰 값으로 교체한다.

lt = 1
rt = largest
```

##### 이분 검색

* lt와 rt 가 같아질 때 res에 요구한 값이 저장된다.

* mid 값은 문제에서 요구하는 동일한 랜선의 길이가 된다.

* **Count 함수**는 cnt 변수를 가진다. **cnt 변수**는 mid(동일한 랜선의 길이) 를 주어진 값들(802,743...)에 나누었을 때 몇 개의 랜선을 가질 수 있는지 체크하고 cnt 값을 반환한다.

* ```python
  def Count(len) :
      cnt = 0
      for x in Line :
          cnt += (x // len) #ex) 802 에서 401로 몇 개를 만들 수 있는지
      return cnt
  ```

* cnt 값이 N보다 작다는건 mid(동일한 랜선의 길이)가 요구하는 값 보다 크다는 뜻이기 때문에 rt에 -1을 해준다.

* cnt 값이 N 보다 크거나 같아지면 mid 값을 더 키워도 된다는 의미이기 때문에 lt에 +1를 해준다.

* lt는 점점 rt와 가까워 지면서 두 변수가 같아질 때 요구하는 값이 저장되고 while문에서 탈출한다.

```python
while lt <= rt :
    mid = (lt + rt) //2 # 동일한 랜선의 길이
    if Count(mid) >= N :
        res = mid
        lt = mid +1
    else :  #길이가 너무 길다
        rt = mid - 1
print(res)       
```