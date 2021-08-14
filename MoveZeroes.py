array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def solution(arr):
    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(0)
    print(arr)

solution(array1)
solution(array2)