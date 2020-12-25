import sys
#sys.stdin = open("data/in2.txt", "rt")
N = int(sys.stdin.readline())

#내 풀이와 강의 풀이가 같다.
scoring = list(map(int,sys.stdin.readline().split()))
score = [0] * N
max_num = 0
cnt = 0
for i, x in enumerate(scoring) :
    if x == 1 :
        cnt += 1
        score[i] = 1
        max_num += cnt
    else :
        cnt = 0
    
print(max_num)
