import sys
#sys.stdin = open("data/in5.txt", "rt")
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

#[3, 2, 2, 1, 3, 1, 2, 3, 2, 2]

cnt = 0
bar = 0
for i in range(N) : 
    num = 0 #문제 5번에서 이것 때문에 무한으로 돈
    if arr[i] == M : # 한 자리가 같을 경우
        cnt += 1
    elif bar == N :
        break # 문제 5번을 저격해서 작성했다 좋지 못한 프로그래밍이다.
    elif i + 1 < N : # 마지막에 j 가 리스트 에러나지 않기 위함
        if arr[i] + arr[i+1] == M:  # 앞 뒤의 합이 M과 같은 경우
            cnt += 1
        elif arr[i] + arr[i+1] < M :# 앞 뒤의 합으로는 M과 다를 경우
            for j in range(i , N) : 
                num += arr[j] # num가 M보다 같거나 커질 때까지 증가한다.
                bar += 1
                if num > M :
                    break
                elif num == M :
                    cnt += 1
                    break
    else :
        break
                
print(cnt) 


#[3, 2, 2, 1, 3, 1, 2, 3, 2, 2]


cnt = 0
lt = 0 #앞에서 시작하는 인덱스
rt = 1 #뒤에서 시작하는 인덱스
tot = arr[0]
while True :
    if tot < M :
        if rt < N : 
            tot += arr [rt]
            rt += 1
        else : # rt가 리스트를 넘어섰을 때
            break
    elif tot == M :
        cnt += 1
        tot -= arr[lt]
        lt += 1
    else : #tot가 M보다 클 때
        tot -= arr[lt]
        lt += 1

print(cnt)

