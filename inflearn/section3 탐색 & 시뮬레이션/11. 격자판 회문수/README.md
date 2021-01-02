## 격자판 회문수

#### 내 풀이

##### 초기 변수

```python
#input
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5
#output
3

a = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]
cnt = 0
```

##### 반복문 사용

* ch1, ch2 리스트를 생성해서  행과 열의 값을 저장한다.

* ch1_mi, ch2_mi 리스트를 생성하고 **반복문을 사용해서 값을 5개씩 끊어서 저장한다.**

* ```python
  2 4 1 5 3 2 6
  
  2 4 1 5 3
  4 1 5 3 2
  1 5 3 2 6
  ```

* ch1_mi, ch2_mi 에 저장한 값이 `[::-1]` 뒤집은 값과 같다면 cnt에 1을 누적한다.

```python
for i in range(7) :
    ch1 = [] #행 값 저장
    ch2 = [] #열 값 저장
    for j in range(7) :
        ch1.append(a[i][j])
        ch2.append(a[j][i])
    
    for j in range(3) :
        ch1_sm = ch1[0+j:5+j]
        ch2_sm = ch2[0+j:5+j]
        if ch1_sm == ch1_sm[::-1] :
            cnt += 1
        if ch2_sm == ch2_sm[::-1] :
            cnt += 1
         
print(cnt)
```



#### 강의 풀이

##### 초기 변수

> 내 풀이와 같다

##### 반복문 사용

* 아래와 같은 코드를 사용한 이유는 내 풀이와 같은 이유이다.

* ```python
  2 4 1 5 3 2 6
  
  2 4 1 5 3
  4 1 5 3 2
  1 5 3 2 6
  
  for i in range(3) :
      for j in range(7) :
  ```

##### 행 조회

````python
#행 조회
tmp = a[j][i:i+5]
# 뒤집은 값과 같을 때
if tmp == tmp[::-1] :
    cnt += 1
````

##### 열 조회

* for문을 한 번 더 사용했다.
* 행 조회처럼 한 번에 비교하는게 아닌 하나씩 비교한다.
* 길이가 5개이기 때문에 `5 // 2 `= 2번 비교한다.

```python
#열 조회
for k in range(2) :
    if a[i+k][j] != a[i+5-k-1][j] :
        break
esle:
    cnt += 1
```

-------

````python
cnt = 0
for i in range(3) :
    for j in range(7) :
        #행 조회
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1] :
            cnt += 1
        #열 조회
        for k in range(2) :
            if a[i+k][j] != a[i+5-k-1][j] :
                break
        else:
            cnt += 1
print(cnt)
````



#### 후기

> 강의 풀이와 접근 방법이 비슷했다.
>
> 이번 풀이는 강의 풀이보다 내 풀이가 조금 더 편했던 것 같다.