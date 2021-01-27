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



##### 평균

> 주어진 수의 합을 측정개수로 나눈 값으로, 대표값 중 하나

##### 분산

> 변량들이 퍼져있는 정도, 분산이 크면 들죽날죽 불안정하다는 의미

##### 표준편차

> 분산은 수치가 너무 커서, 제곱근으로 적당하게 줄인 값

출처 : https://learnx.tistory.com/entry/%ED%86%B5%EA%B3%84%EC%9D%98-%EA%B8%B0%EC%B4%88%EC%9D%B8-%ED%8F%89%EA%B7%A0-%EB%B6%84%EC%82%B0-%ED%91%9C%EC%A4%80%ED%8E%B8%EC%B0%A8





#### N이 주어지지 않았을 때 배열 받기

* input을 문자열로 받아서 for문을 이용해 형변환을 해준다.

```java
BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
//문자열 숫자 배열로 input 받기
String[] s = bf.readLine().split(" ");
//형변환할 배열
int[] tower_list = new int[s.length];

for(int i = 0; i < s.length; i++){
	//문자열 -> 정수 형변환
	tower_list[i] = Integer.parseInt(s[i]);
}
```

