#### BufferedReader

> 버퍼를 이용해서 읽고 쓰는 함수입니다.
>
> 버퍼를 이용하면 입출력의 효율이 좋아집니다.
>
> 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 **임시 메모리 영역**
>
> **입출력 속도 향상**을 위해 버퍼를 사용
>
> * 입력 : BufferedReader
> * 출력 : BufferedWriter



![buffer](C:\Users\82108\LMH\coding_test\TIL-for-MyungHo\기타\image\buffer.png)

> 예를 들자면, 흙을 파서 저 언덕에 버리는데, 한 번 삽질할 때마다 가서 버리는 것보다, 수레에 가득 채워서 **한번에 나르는 것이 효율적**인 것과 같은 이치. 즉 모아뒀다가 한번에 전송하는게 훨씬 효율적이다.



#### csv 파일 가져오기

```java
BufferedReader br = null;
//파일 읽기
br = Files.newBufferedReader(Paths.get("C:\\Users\\82108\\LMH\\workspace\\BRIQUE\\src\\sample.csv"));
//p1, p2, p3, p4 .....
String line = br.readLine();
```

