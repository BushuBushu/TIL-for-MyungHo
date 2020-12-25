import sys
# sys.stdin = open("data/in1.txt", "rt")

T = int(sys.stdin.readline())

for i in range(T) :
    N, s, e, k = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))
    array = array[s - 1 : e ]
    array.sort()

    print("#%d %d" %(i + 1, array[k-1]))
