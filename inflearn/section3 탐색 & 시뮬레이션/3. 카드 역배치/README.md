## 카드 역배치

#### 스왑하는 방법

````python
a, b = map(int, sys.stdin.readline().split())
print(a, b) # 5 10
a, b = b, a
print(a, b) # 10 5

#내 풀이
arr_reverse = arr[a-1:b] # index arr[4] =5부터 arr[10] =9 전까지 5,6,7,8,9
arr_reverse.reverse() # 9 8 7 6 5
arr[a-1:b] =  arr_reverse # 해당 리스트 반전

#강의는 이런식으로 사용
for i in range((e-s+1)//2) : #(10-5+1)//2 = 3 
    # i = 0,1,2
    a[s+i], a[e-i] = a[e-i], a[s+i] #5,10=10,5 6,9=9,6...
````



#### 후기

* 나는 전체를 한 번에 바꾸는 방법을 사용했는데 강의에서는 하나하나 비교하면서 바꾸는 방법을 사용했다.

