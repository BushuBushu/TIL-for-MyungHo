import sys
#sys.stdin = open("data/in3.txt", "rt")

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
index = 0
arrMin = float('inf')
div = 0

div = round(sum(arr)/N)

for i in range(len(arr)):
    if abs(div - arr[i]) < arrMin :
        arrMin = abs(div - arr[i])
        index = i

    elif abs(div - arr[i]) == arrMin :
        if arr[index] < arr[i] :
            arrMin = abs(div - arr[i])
            index = i
            
print("%d %d" %(div, index + 1))

