import sys
#sys.stdin = open("data/in2.txt", "rt")
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

# 내풀이

def reverse(x) :
    num = str(x)[::-1] #처음부터 끝까지 C 의 간격으로
    if num[0] == "0":
        num = num[1:] #앞의 수가 0인 값은 index 1부터 시작
    num = int(num)
    return num

def isPrime(x) :
    if x == 1 : # 1이 출력 되면 안 되기 때문에   false 반한
        return False
    for i in range(2, x // 2 + 1): # ex) 16일 때 1 * 16 , 2 * 8인데 2부터는 절반 값만 확인하면 
        if x % i == 0 :
            return False
    else :
        return True

  
for x in arr :
    reverse_num = reverse(x)
    if isPrime(reverse_num) :
        print(reverse_num, end=' ')
'''
#강의 풀이
def reverse(x):
    res = 0
    while x > 0:
        t = x%10
        res = res * 10 + t
        x = x//10
    return res

def isPrime(x) :
    if x == 1 :
        return False
    for i in range(2, x//2 + 1):
        if x%i == 0:
            return False
    else:
        return True

for x in arr :
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end = ' ')
'''
