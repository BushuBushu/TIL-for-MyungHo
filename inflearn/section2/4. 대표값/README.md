## 대표값

#### 음수를 양수로변환 abs()

```python
a = -1
print(-a) #1

#배열에서 음수 양수 모두 양수로 바꾸기
abs(a)
print(a) #1
```

#### enumerate

```python
a = [1,2,3,4,5,6]
#enumerate(a) : idx에는 index 번호, x에는 값이 할당
for idx, x in enumerate(a) :
	
```

#### round

round()는 사사오입 원칙을 따른다. 반올림할 자리의 수가 5이면 반올림 할 때 앞자리의 숫자가 짝수면 내림하고 홀수면 올림 한다.

우리가 흔히 말하는 반올림 방식은 **round_half_up** 방식이다. 

파이썬에서 **round**는 **round_half_even **  방식이다

*  ````python
  round(4.5)  #결과는 4
  round(3.5)  #결과는 4
   ````



* ````python
  import math
  
  a = 66.5
  
  #0.5를 더해주고 내림
  #66.5이상이면 67이 되고, 65.5 미만이면 66이 된다.
  a = math.floor(a + 0.5)
  a = int(a)
  print(a)
  ````

