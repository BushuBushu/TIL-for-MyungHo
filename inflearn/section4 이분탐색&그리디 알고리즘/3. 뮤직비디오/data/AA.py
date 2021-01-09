import sys
#sys.stdin = open("data/in6.txt", "rt")
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

def Count(len) :
    cnt = 0
    num = 0
    for x in a :
        if num + x > len :
            cnt += 1
            num = x
        else:
            num += x
    if num >= 1 :
        cnt += 1
    return cnt  
    
lt = 1
rt = sum(a)
while lt <= rt :
    mid  = (lt + rt) // 2 #23, 11
    if Count(mid) <= M : #3
        res = mid
        rt = mid - 1
    else :
        lt = mid + 1
print(res)
'''    
import sys
sys.stdin = open("data/in1.txt", "rt")
def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m=map(int, input().split())
Music=list(map(int, input().split()))
maxx=max(Music)
lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)
'''
