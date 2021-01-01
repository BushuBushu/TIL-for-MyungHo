import sys
#sys.stdin = open("data/in5.txt", "rt")

a = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
'''
for i in a :  
    print(i)
'''
true_list = [1] * 9
end = True #3*3 실행에 대한 조건
for i in range(9) :
    z_list = [0] * 9 # 가로 누적
    x_list = [0] * 9 # 세로 누적
    p = 0 #세로 인덱스
    for j in range(9) :
        #가로
        z_list[ a[i][j] -1 ] = 1
        #세로
        x_list[ a[j][p] -1 ] = 1
    p += 1
    if z_list != true_list or x_list != true_list:
        print("NO")
        end= False
        break

no = False # 3*3에서 NO가 출력되면 for문을 빠져나온다.
if end :
    for i in range(0,9,3) :
        for j in range(0,9,3) : #i 0 j 0
            c_list = [0] * 9 # 3*3 누적
            c_list[ a[i][j] -1 ] = 1 #00
            c_list[ a[i][j+1] -1 ] = 1 #01
            c_list[ a[i][j+2] -1 ] = 1 #02
            
            c_list[ a[i + 1][j] -1 ] = 1 #10
            c_list[ a[i + 1][j+1] -1 ] = 1 #11
            c_list[ a[i + 1][j+2] -1 ] = 1 #12
            
            c_list[ a[i + 2][j] -1 ] = 1 #20
            c_list[ a[i + 2][j+1] -1 ] = 1#21
            c_list[ a[i + 2][j+2] -1 ] = 1 #22
            
            if c_list != true_list :
                no = True
                print("NO")
                break
        if no :
            break
    else :
        print("YES")


