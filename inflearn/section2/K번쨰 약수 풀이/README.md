## K번째 약수 풀이

### sys.stdin
* Python에서 입력 값을 받을 때 input()보다 시간 단축을 위해 sys.stdin을 사용한다.

* 한 라인을 입력 받을 때

  ```python
   sys.stdin.readline()
   #한 번에 값 두개 받기
   N, K = sys.stdin.readline().split
  ```

  

* 여러 줄을 입력 받을 때

  ```python
  for line in sys.stdin :
  ```

  

### 약수
p와 q가 있을 때,  만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.