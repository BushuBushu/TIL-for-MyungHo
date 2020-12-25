import sys
sys.stdin = open("data/in6.txt", "rt")
N = int(sys.stdin.readline())

#내 풀이 (강의 풀이가 훨씬 효율적이다.)
num_max = -2400000 #최대 점수
for i in range(N) :
    arr = list(map(int, sys.stdin.readline().split())) #[3, 3, 6] [0, 0, 0] [0, 0, 0] ...
    cnt = 0 # 같은 수가 몇 개인지 저장 됨
    num = 0 #점수 계산
    for j, x in enumerate(arr) : #3 3 6 따로 출력
        cnt_check = 0 # cnt 저장 전 카운팅
        for k, y in enumerate(arr) :
            if arr[j] == arr[k] : #[0] == [1][2][3] ... 
                cnt_check += 1 
        if cnt < cnt_check : # cnt _check 중에서 가장 큰 값을 저장
            cnt = cnt_check
    if cnt == 3 :
        num = 10000 + (arr[0] * 1000)
        
    if cnt == 2 :
        for q, a in enumerate(arr) :
            cnt_check = 0
            for k, y in enumerate(arr) :
                if arr[q] == arr[k] :
                    cnt_check += 1
            if cnt_check == 2 :
                num = 1000 + (a * 100)
                break ##cnt_check 가 2가 될 때의 a 값은 중복 값이기 때문에 사용
            
    if cnt == 1 :
        arr.sort(reverse = True)
        num = arr[0] * 100 

    if num_max < num :
        num_max = num
     
print(num_max)


# 강의 풀이
res = 0
for i in range(N) :
    tmp = list(sys.stdin.readline().split())
    tmp.sort() # 미리 정렬을 해둔다
    a, b, c = map(int, tmp) #list를 a, b ,c 각각 변수에 저장
    if a == b and b ==c : # abc가 모두 같을 때
        money = 10000 + (a * 1000)
    elif a == b or a == c : #abc 중 2개만 같은 때
        money = 1000 + (a * 100)
    elif b == c : #abc 중 2개만 같은 때
        money = 1000 + (b * 100)
    else :
        money = c * 100
    if money > res :
        res = money
print(res)
