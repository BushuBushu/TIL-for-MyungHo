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

#### 연결 방식

|      |        |
| ---- | ------ |
| %f   | 실수   |
| %d   | 정수   |
| %s   | 문자열 |

```python
#예시

a = 1
b = 2
print("#%d %d" %(a, b)) # #1 2

#%뒤에 있는 a와 b를 %d로 대체한다.
```

