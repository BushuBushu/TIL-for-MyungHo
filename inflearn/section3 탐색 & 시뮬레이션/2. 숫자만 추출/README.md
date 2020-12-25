## 숫자만 추출



#### isdecimal

> 0부터 9까지의 숫자만 찾아줌
>
> 숫자가 있으면 True를 반환함

```python
N = "kdk1k0kdjfkj0kkdjkfj0fkd"

for x in N :
    if x.isdecimal() :
        res = res * 10 + int(x)
```



#### isdigit

> 숫자 형태는 다 찾아줌
>
> 2의 2승 등등의..



#### 아쉬운점

* isdecimal 이라는 걸 몰라서 내 손으로 못 풀었다..