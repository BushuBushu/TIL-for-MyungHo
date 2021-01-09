## 뮤직 비디오 (결정알고리즘)



#### 이론 듣고 풀이

##### 초기 변수

`````python
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

9 3
1 2 3 4 5 6 7 8 9
`````

##### lt, rt, mid를 사용한 반복문

* ```python
  lt = 1, mid = 23, rt = 45 #cnt 3
  lt = 1, mid = 11, rt = 22 #5
  #lt = 12, mid = 17, rt = 22 #3
  lt = 12, mid = 14, rt = 16 #5
  lt = 15, mid = 15, rt = 16 #4
  lt = 16, mid = 16, rt = 17 #4
  ```

* M값이 cnt 보다 크거나 같을 때만 res에 값 저장한다.

  * M = 3 일 때 cnt = 3 보다 작으면 res에 mid 값 저장, 3보다 크면 무시.

* ##### count 함수

* ```python
  def Count(len) :
      cnt = 0
      num = 0
      for x in a :
          if num + x > len :
              cnt += 1
              num = x
          else:
              num += x
      # 마지막 num에 저장되어 있는 수는 len 보다 작기 때문에 남은 값이 있을 때 cnt + 1
      if num >= 1 :
          cnt += 1
      return cnt  
  ```

* 

````python
lt = 1
rt = sum(a)
while lt <= rt :
    mid  = (lt + rt) // 2 #23, 11
    if Count(mid) <= M :
        res = mid
        rt = mid - 1
    else :
        lt = mid + 1
print(res)
````



#### 반례 수정

##### 예시

````
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

9 9
1 2 3 4 5 6 7 8 9
````

* 주어진 M이 리스트의 가장 큰 값과 같을 경우 rt가 1까지 떨어져 res = 1이 되게 된다.

* ```python
  #rt가 1이 될 때까지 cnt가 계속 증가하게 됨
  3
  5
  8
  9
  9
  ```

* 이러한 경우를 방지하기 위해 리스트 중 **가장 큰 값**이 필요하다.

  * mid가  maxx 보다 클 경우에만 Count 함수를 실행하고 rt가 감소한다.

  * mid가 maxx 보다 잘을 경우에는 lt가 증가한다.

  * ```python
    if mid>=maxx #일 때
    #cnt 
    3
    5
    6
    ```

  * 

* ```python
  # 리스트 중 가장 큰 노래
  maxx=max(Music)
  while lt<=rt:
      mid=(lt+rt)//2
      # 용량이 가장 큰 노래보다 mid는 크거나 같아야 한다. 
      if mid>=maxx and Count(mid)<=m:
          res=mid
          rt=mid-1
      else:
          lt=mid+1
  ```