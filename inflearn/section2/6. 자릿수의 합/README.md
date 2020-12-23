## 자릿수의 합

#### 자릿수 구하기

정수 값의 자릿수를 구하기 위해서는 **문자열로 형변환**을 해주어야 한다.

````python
a = 12345
print(a[0]) #error

#string 형변환
num = str(a)
print(num[0]) #1

#for문 str 사용
for i in str(x) :
    sum += int(i)
return sum
````

전역 변수를 지역 범위에서 사용하고 싶으면 global 표현을 사용한다.

 