import sys
sys.stdin = open("data/in3.txt", "rt")
N = int(sys.stdin.readline())

#내 풀이

for i in range(N) :
    arr = list(sys.stdin.readline().split()) 
    result = "" # index 0부터 절반까지 문자열
    result_reverse = "" # 절반부터 마지막까지 문자열
    for j, x in enumerate(arr) :
        x = x.lower() # 문제에 소문자 대문자 상관 안 한다고 했음
        result = x[0:len(x) // 2] #전체 길이에서 2로 나누었을 때의 몫 홀수 길이일 때 중간 값 저장 x
        if len(x) % 2 == 0 : 
            result_reverse= x[(len(x) // 2) : len(x)] # 문자열이 짝수일 때 중간부터 시작
            result_reverse = result_reverse[::-1] # 중간 이후 문자열을 뒤집는다.
        else :
            result_reverse= x[(len(x) // 2)+1 : len(x)] #문자열이 홀수일 때 중간 제외 시작
            result_reverse = result_reverse[::-1]
            
    if result == result_reverse : 
        print('#%d %s' %(i + 1,'YES'))
    else:
        print('#%d %s' %(i + 1,'NO'))

#강의 풀이
for i in range(N):
    s = input()
    s = s.upper() #전부 대문자로 변경
    size = len(s)
    for j in range(size // 2) :
        if s[j] != s[-1 -j] :
            print('#%d NO' %(i + 1))
            break
    else :
        print('#%d YES' %(i + 1))

#강의 풀이 (더 짧게)
for i in range(N):
    s = input()
    s = s.upper() #전부 대문자로 변경
    if s == s[::-1] : # 뒤집은 것과 같을 때 
        print('#%d YES' %(i + 1))
    else :
        print('#%d NO' %(i + 1))
        
        
