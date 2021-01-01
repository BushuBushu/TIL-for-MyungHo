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
* 세로 리스트는 p 변수를 사용해서 for문이 돌 때마다 1을 누적해서 열을 조회한다.

```python
true_list = [1] * 9 [1,1,1,1,1,1,1,1,1]
end = True #3*3 실행에 대한 조건
for i in range(9) :
    z_list = [0] * 9 # 가로 누적
    x_list = [0] * 9 # 세로 누적
    p = 0 #세로 인덱스
    for j in range(9) :
        #가로
        z_list[ a[i][j] -1 ] = 1
        #세로
        x_list[ a[j][p] -1 ] = 1
    p += 1
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