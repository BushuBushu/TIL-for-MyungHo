import sys
# sys.stdin = open("data/in1.txt", "rt")

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
# [18 54 46 52 28 22 23 53 28 40 ]

count = 0
result = 0
arr2 = []
# 세 개의 카드를 뽑는 요구 사항
for i in range(N) :
    for j in range(i + 1, N) : # i랑 안 겹치는 1부터 시작
        for x  in range(j + 1, N) : # j랑 안 겹치는 2부터 시작
            result = 0
            result = arr[i] + arr[j] + arr[x]
            arr2.append(result) 
            

arr2 = sorted(set(arr2), reverse = True) #내림차순 정렬 후 중복 제거
arr2 = list(arr2) # 다시 배열 형식으로 변경

print(arr2[K - 1]) # index 순서와 맞추기 위해 -1
