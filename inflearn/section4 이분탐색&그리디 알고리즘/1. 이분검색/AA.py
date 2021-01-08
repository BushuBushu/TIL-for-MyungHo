import sys
#sys.stdin = open("data/in1.txt", "rt")
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

lt = 0
rt = N - 1

while True :
    mid = (lt + rt) //2
    if a[mid] == M :
        print(mid + 1)
        break
    elif a[mid] > M :
        rt = mid - 1
    elif a[mid] < M :
        lt = mid + 1
