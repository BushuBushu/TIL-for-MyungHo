## 주사위 게임

#### for문에서 변수에 list 값 할당

```python
for i in range(N) :
    tmp = list(sys.stdin.readline().split())
    tmp.sort() # 미리 정렬을 해둔다
    a, b, c = map(int, tmp) #list를 a, b ,c 각각 변수에 저장
```



#### 내 풀이 아쉬운 점

생각해보니 처음부터 sort를 사용했으면 더 편했을 텐데...

아직 파이썬의 문법이 익숙하지 않아 쓸대 없는 코드의 길이가 길어졌다 

좀 더 클린 코드를 작성할 수 있도록 노력해야겠다.