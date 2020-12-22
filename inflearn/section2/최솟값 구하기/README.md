## 최솟값 구하기

```python
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') #무한대

for i in arr:
    if i < arrMin:
        #첫번째 수는 무한대 보다 무조건 작을 수 밖에 없다.
        # <= 로 비교하면 더 뒤에 있는 중복 값으로 변경
        arrMin = i
print(arrMin)

```

