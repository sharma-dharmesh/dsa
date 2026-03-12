def bubbleSort(arr):
    flag = 0
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            break
    
arr1 = [5,3,1,7,8, 9, 2]
bubbleSort(arr1)
print(arr1)