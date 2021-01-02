## 스도쿠 검사

#### 내 풀이 (좋지 못한 코드를 작성한 것 같다.)

##### 초기 변수

```python
1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7

a = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
```

##### 가로 세로 조회

* a 리스트의 가로와 세로에 저장된 값을   `z_list[]`,`x_list[]` 에 인덱스 값으로 넣어준다 

```python
true_list = [1] * 9 [1,1,1,1,1,1,1,1,1]
end = True #3*3 실행에 대한 조건
for i in range(9) :
    z_list = [0] * 9 # 가로 누적
    x_list = [0] * 9 # 세로 누적
    for j in range(9) :
        #가로
        z_list[ a[i][j] -1 ] = 1
        #세로
        x_list[ a[j][p] -1 ] = 1
    if z_list != true_list or x_list != true_list:
        print("NO")
        end= False
        break
```

##### 3*3 조회

* 0, 3, 6 순서대로 실행된다.
* 아홉개의 인덱스를 수기로 작성했다 좀 더 좋은 코드가 있을 것으로 생각이든다.

```python
no = False # 3*3에서 NO가 출력되면 for문을 빠져나온다.
if end :
    for i in range(0,9,3) :
        for j in range(0,9,3) : #ex) i = 0, j = 0
            c_list = [0] * 9 # 3*3 누적
            c_list[ a[i][j] -1 ] = 1 #00
            c_list[ a[i][j+1] -1 ] = 1 #01
            c_list[ a[i][j+2] -1 ] = 1 #02
            
            c_list[ a[i + 1][j] -1 ] = 1 #10
            c_list[ a[i + 1][j+1] -1 ] = 1 #11
            c_list[ a[i + 1][j+2] -1 ] = 1 #12
            
            c_list[ a[i + 2][j] -1 ] = 1 #20
            c_list[ a[i + 2][j+1] -1 ] = 1#21
            c_list[ a[i + 2][j+2] -1 ] = 1 #22
            
            if c_list != true_list :
                no = True
                print("NO")
                break
        if no :
            break
    else :
        print("YES")
```



#### 강의 풀이

* **행, 열, 3*3 그룹**을 **체크하는 리스트**가 필요하다.

* 함수가 True를 리턴하면 YES. False를 리턴하면 NO를 출력한다.

* 행과 열을 체크하는 부분은 내 풀이와 비슷했지만 **3*3그룹 조회**하는 부분은 강의에서는 **4중 for문**을 사용했다.

* ```python
  			j
      ---------------------
    |  1 4 3  6 2 8  5 7 9
    |  5 7 2  1 3 9  4 6 8
    |  9 8 6  7 5 4  2 3 1
  i |
    |  3 9 1  5 4 2  7 8 6
    |  4 6 8  9 1 7  3 5 2
    |  7 2 5  8 6 3  9 1 4
    |
    |  2 3 7  4 8 1  6 9 5
    |  6 1 9  2 7 5  8 4 3
    |  8 5 4  3 9 6  1 2 7
      
         k
       ------
      | 1 4 3
    s | 5 7 2
      | 9 8 6
  
  #4중 for문 사용
  --------------------------------- #3*3 그룹 생성
  
      for i in range(3) : #3을 곱해서 전체 그룹의 행을 0 3 6씩 조회
          for j in range(3) : #3을 곱해서 전체 그룹의 열을 0 3 6씩 조회
              
  ---------------------------------- #여기까지 총 9그룹을 조회         
              ch3 = [0] * 10
              for k in range(3) : #한 그룹의 행
                  for s in range(3) : #한 그룹의 열
                      ch3[a[i * 3 + k][j * 3 + s]] = 1
  ```

  

```python
def check(a) :
    #행과 열 조회
    for i in range(9) :
        ch1 = [0] * 10 #행을 체크
        ch2 = [0] * 10 #열을 체크
        for j in range(9):
            ch1[ a[i][j] ] = 1
            ch2[ a[j][i] ] = 1
        if sum(ch1) !=9 or sum(ch2) !=9 :
            return False
        
    #3 * 3 그룹 조회 
    #4중 for문 사용
    for i in range(3) : #0 1 2
        for j in range(3) : #0 1 2
            ch3 = [0] * 10
            for k in range(3) :
                for s in range(3) :
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9 :
                return False
    return True
```

```python
if check(a):
    print("YES")
else:
    print("NO")
```





#### 후기

> 내 풀이와 강의 풀이의 문제 접근 방법이 비슷했다. 문제를 푸는 능력이 조금 성장한 것 같아 뿌듯하다.