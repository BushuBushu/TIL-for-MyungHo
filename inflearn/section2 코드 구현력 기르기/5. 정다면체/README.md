## 정다면체

#### 구하는 법

예를 들어 정사면체와 정육면체를 굴려 나올 수 있는 합 중 가장 확률이 높은 숫자를 구한다.

나올 수 있는 합 : 1 ~ 10 (4 + 6)

가장 많이 나온 합의 최대 갯수 : 4 (둘 중의 작은 정다면체의 수)

가장 많이 나온 합의 수  : 5, 6, 7 (정사면체의 4 부터 정육면체의 6 그리고 + 1)

```
1 2 3 4
1 2 3 4 5 6

1 2 3 4 5 6 7 8 9 10 #합
0 1 2 3 4 4 4 3 2 1
```

#### 배열 0 초기화

````python
count = [0] * 10
[0,0,0,0,0,0,0,0,0,0]
````

