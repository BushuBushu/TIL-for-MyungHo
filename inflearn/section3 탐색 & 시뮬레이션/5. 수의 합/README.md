## 수들의 합

#### 연속 부분합

**lt ~ rt** 의 바로 전 까지의 합 



#### 변수 지정

````python
N, M = map(int, sys.stdin.readline().split()) # 10, 5
arr = list(map(int, sys.stdin.readline().split()))
#[3, 2, 2, 1, 3, 1, 2, 3, 2, 2]

lt = 0 #앞에서 시작하는 인덱스
rt = 1 #뒤에서 시작하는 인덱스
cnt = 0
tot = arr[0]
````

|       | lt   | rt   |      |      |      |      |      |      |      |      |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| index | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
| list  | 3    | 2    | 2    | 1    | 3    | 1    | 2    | 3    | 2    | 2    |

```python
#rt가 1일 때
tot = 3
rt +1
#rt가 2일 때 
tot = 5 #M과 같아짐
lt +1
tot = tot - arr[lt] # 2

#lt = 1 rt = 2가 된다.
```

````python
tot = [lt : rt]

tot < M # rt 증가
tot == M # lt 증가
tot > M # lt 증가
````

#### 반복문

````python
while True :
#rt가  N보다 커지거나 같아질 경우 break
````

#### tot < M

````python
if tot < M :
    if rt < N : 
        tot += arr [rt]
    	rt += 1
    else : # rt가 리스트를 넘어섰을 때
        break
````

#### tot == M

````python
elif tot == M :
    cnt += 1
    tot -= arr[lt]
    lt += 1
````

#### tot > M

```python
else : #tot가 M보다 클 때
        tot -= arr[lt]
        lt += 1
```

