## K번째 수

#### list에 값을 int로 저장

빈 변수에 여러 input 값을 넣어주면 list 형태가 된다.

```python
# X
a = map(int, sys.stdin.readline().split())

# O
a = list(map(int, sys.stdin.readline().split()))
```



####  list i번 부터 j 번 까지 출력

```python
list = list[i - 1 : j - 1]
```

