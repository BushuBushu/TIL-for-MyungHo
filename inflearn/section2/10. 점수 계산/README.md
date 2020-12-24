## 점수 계산

채점한 항목이 1(정답)일 때 count를 +1 해준다.

정답이 연속 되면 count의 값이 초기화 되지 않고 쌓인다

오답 (0)이 되면 count의 점수가 0으로 초기화 된다.

```python
for i, x in enumerate(scoring) :
    if x == 1 :
        cnt += 1
        score[i] = 1
        max_num += cnt
    else :
        cnt = 0
```

