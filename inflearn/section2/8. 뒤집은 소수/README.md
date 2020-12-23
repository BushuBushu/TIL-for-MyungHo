## 뒤집은 소수

#### 숫자를 뒤집기 

```python
a = 123
num = str(a)[::-1]
#[A:B:C] A부터 B까지 C의 간격
#[::C] 처음부터 끝까지 C 의 간격으로
#[::-1] 경우에는 반대 출력 # 321

#다른 방법으로는 
def reverse(x): # x = 3700
    res = 0
    while x > 0:
        t = x % 10 # t = 0 0 7 3
        res = res * 10 + t # res = 0 0 7 73
        x = x//10 # x = 073 73 3 0
    return res
```



